#!/usr/bin/env python3
"""
Export GitHub Issues (used as a personal notes system) into a folder structure
suitable for dragging into Notion:

    ./<issue_title>/<datetime>_<comment_title>.md

Each issue = one topic/folder. Each comment (plus the issue's own opening
body) = one note file. Images referenced in note bodies are downloaded
locally next to the note and the markdown is rewritten to point at the
local copy.

Notes are written and committed to git one at a time, in chronological
order, with the commit's author/committer date set to the note's real
GitHub creation timestamp -- so `git log` reflects the actual note-taking
timeline instead of the day this script was run. Git operations are kept
strictly sequential (required for correct ordering); the network-bound
work -- fetching comments per issue and downloading images -- is done
concurrently ahead of time with a bounded thread pool and retry/backoff,
so a slow network doesn't serialize the whole run but a burst of requests
also doesn't trip GitHub's rate limiting.

Usage:
    venv/bin/python scripts/export_notes.py [--repo owner/name] [--out DIR] [--issue N] [--no-commit] [--workers N]

Requires `gh` to be authenticated (gh auth login) for a decent API rate limit.
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

DEFAULT_REPO = "solomonxie/study-notes"
DEFAULT_WORKERS = 6
IMG_EXT = r'png|jpe?g|gif|webp|svg'
IMG_MD_RE = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
IMG_HTML_RE = re.compile(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*>')
# A plain (non-image) markdown link whose target is itself an image file --
# GitHub still renders these as clickable thumbnails, so treat them the same.
IMG_LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\((https?://[^)\s]+\.(?:' + IMG_EXT + r'))\)')
# A bare image URL on its own line (no markdown wrapper at all) -- GitHub
# auto-embeds these when rendering, so mirror that when exporting.
IMG_BARE_RE = re.compile(r'^([ \t]*)(https?://\S+\.(?:' + IMG_EXT + r'))[ \t]*$', re.MULTILINE)


def with_retry(fn, *, attempts: int = 5, base_delay: float = 2.0, what: str = "request"):
    """Run fn() with exponential backoff on transient/rate-limit failures."""
    last_exc = None
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except RateLimited as e:
            last_exc = e
            delay = e.retry_after or (base_delay * (2 ** (attempt - 1)))
            print(f"    ! rate limited on {what}, backing off {delay:.0f}s (attempt {attempt}/{attempts})", file=sys.stderr)
            time.sleep(delay)
        except Exception as e:
            last_exc = e
            if attempt == attempts:
                break
            delay = base_delay * (2 ** (attempt - 1))
            print(f"    ! {what} failed ({e}), retrying in {delay:.0f}s (attempt {attempt}/{attempts})", file=sys.stderr)
            time.sleep(delay)
    raise last_exc


class RateLimited(Exception):
    def __init__(self, retry_after: float | None = None):
        self.retry_after = retry_after


def run_gh(args: list[str]) -> str:
    result = subprocess.run(["gh"] + args, capture_output=True, text=True)
    if result.returncode != 0:
        err = result.stderr
        if "rate limit" in err.lower() or "403" in err:
            raise RateLimited()
        raise RuntimeError(f"gh {' '.join(args)} failed:\n{err}")
    return result.stdout


def gh_api_paginated(path: str) -> list[dict]:
    out = with_retry(lambda: run_gh(["api", "--paginate", path]), what=f"gh api {path}").strip()
    # --paginate with multiple pages concatenates separate JSON arrays; handle both.
    items: list[dict] = []
    decoder = json.JSONDecoder()
    idx = 0
    while idx < len(out):
        while idx < len(out) and out[idx] in " \t\n\r":
            idx += 1
        if idx >= len(out):
            break
        obj, end = decoder.raw_decode(out, idx)
        items.extend(obj)
        idx = end
    return items


def slugify(text: str, max_len: int = 80) -> str:
    # Keep Unicode (e.g. Chinese) intact -- only strip characters unsafe in
    # filenames and leading markdown/quote punctuation, and collapse whitespace.
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r'[\/:*?"<>|]', "", text)
    text = re.sub(r"^[#>\s]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return (text or "untitled")[:max_len].strip()


def safe_dirname(text: str) -> str:
    text = re.sub(r'[\/:*?"<>|]', "-", text).strip()
    text = re.sub(r"\s+", " ", text)
    return text or "untitled"


def clean_title_text(text: str) -> str:
    """Strip markdown image/link syntax down to their visible text, so a
    heading that's just an embedded image (or a linked title) doesn't leak
    raw URLs/brackets into a filename."""
    text = IMG_MD_RE.sub(lambda m: m.group(1), text)          # ![alt](url) -> alt
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)      # [text](url) -> text
    return text.strip()


def derive_title(body: str, fallback: str) -> str:
    if not body:
        return fallback
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("#"):
            title = clean_title_text(line.lstrip("#").strip())
            if title:
                return title
            # Heading was just an image with no alt text -- keep looking.
    for line in body.splitlines():
        line = line.strip()
        if line:
            title = clean_title_text(re.sub(r"^[>\s]+", "", line))
            if title:
                return title[:80].strip()
    return fallback


def fetch_bytes(url: str) -> bytes:
    try:
        req = Request(url, headers={"User-Agent": "notes-export"})
        with urlopen(req, timeout=30) as resp:
            return resp.read()
    except HTTPError as e:
        if e.code in (403, 429):
            retry_after = e.headers.get("Retry-After")
            raise RateLimited(retry_after=float(retry_after) if retry_after else None)
        raise
    except URLError:
        raise


def guess_ext(url: str) -> str:
    ext = Path(urlparse(url).path).suffix
    return ext if ext and len(ext) <= 5 else ".png"


def build_note_content(note_title: str, body: str) -> str:
    """Prefix with an H1 title, unless the body already opens with that heading."""
    first_line = next((l.strip() for l in body.splitlines() if l.strip()), "")
    if first_line.startswith("#") and first_line.lstrip("#").strip() == note_title:
        return f"{body}\n"
    return f"# {note_title}\n\n{body}\n"


def extract_image_urls(body: str) -> list[str]:
    urls = [m.group(2) for m in IMG_MD_RE.finditer(body)]
    urls += [m.group(1) for m in IMG_HTML_RE.finditer(body)]
    urls += [m.group(2) for m in IMG_LINK_RE.finditer(body)]
    urls += [m.group(2) for m in IMG_BARE_RE.finditer(body)]
    return [u for u in urls if not u.startswith("data:")]


def prefetch_images(jobs: list["NoteJob"], max_workers: int) -> dict[str, bytes | None]:
    """Download every distinct image URL across all jobs concurrently, ahead of
    the sequential write/commit pass, so network latency doesn't serialize it."""
    urls = sorted({u for job in jobs for u in extract_image_urls(job.body)})
    if not urls:
        return {}
    print(f"Prefetching {len(urls)} distinct images with {max_workers} workers ...")
    cache: dict[str, bytes | None] = {}

    def fetch_one(url: str) -> tuple[str, bytes | None]:
        try:
            data = with_retry(lambda: fetch_bytes(url), what=f"image {url}")
            return url, data
        except Exception as e:
            print(f"    ! failed to download {url}: {e}", file=sys.stderr)
            return url, None

    done = 0
    with cf.ThreadPoolExecutor(max_workers=max_workers) as pool:
        for url, data in pool.map(fetch_one, urls):
            cache[url] = data
            done += 1
            if done % 25 == 0 or done == len(urls):
                print(f"  prefetched {done}/{len(urls)} images")
    return cache


def process_images(body: str, note_dir: Path, note_stem: str, image_cache: dict[str, bytes | None]) -> str:
    """Rewrite image links to local relative paths, using pre-fetched bytes."""
    img_dir = note_dir / f"{note_stem}_files"
    urls_seen: dict[str, str] = {}
    counter = [0]

    def replace_url(url: str) -> str:
        if url in urls_seen:
            return urls_seen[url]
        if url.startswith("data:"):
            return url
        data = image_cache.get(url)
        if data is None:
            # Not prefetched (or prefetch failed) -- fall back to a direct fetch.
            try:
                data = with_retry(lambda: fetch_bytes(url), what=f"image {url}")
            except Exception as e:
                print(f"    ! failed to download {url}: {e}", file=sys.stderr)
                urls_seen[url] = url
                return url
        counter[0] += 1
        img_dir.mkdir(exist_ok=True)
        fname = f"img_{counter[0]:02d}{guess_ext(url)}"
        dest = img_dir / fname
        dest.write_bytes(data)
        rel = f"{note_stem}_files/{fname}"
        urls_seen[url] = rel
        print(f"    saved image -> {rel}")
        return rel

    def md_sub(m: re.Match) -> str:
        return f"![{m.group(1)}]({replace_url(m.group(2))})"

    def html_sub(m: re.Match) -> str:
        return m.group(0).replace(m.group(1), replace_url(m.group(1)))

    def link_sub(m: re.Match) -> str:
        # A plain link to an image file -- re-emit as an embedded image so it
        # previews inline, matching how GitHub renders it.
        return f"![{m.group(1)}]({replace_url(m.group(2))})"

    def bare_sub(m: re.Match) -> str:
        return f"{m.group(1)}![image]({replace_url(m.group(2))})"

    body = IMG_MD_RE.sub(md_sub, body)
    body = IMG_HTML_RE.sub(html_sub, body)
    body = IMG_LINK_RE.sub(link_sub, body)
    body = IMG_BARE_RE.sub(bare_sub, body)
    return body


@dataclass
class NoteJob:
    created_at: str          # ISO 8601, e.g. 2021-11-17T14:21:11Z
    topic_dir: Path
    note_title: str
    body: str
    commit_label: str        # for the commit message


def collect_jobs(repo: str, out_dir: Path, only_issue: int | None, max_workers: int) -> list[NoteJob]:
    print(f"Fetching issue list for {repo} ...")
    issues = gh_api_paginated(f"repos/{repo}/issues?state=all&per_page=100")
    issues = [i for i in issues if "pull_request" not in i]
    if only_issue:
        issues = [i for i in issues if i["number"] == only_issue]
    issues.sort(key=lambda i: i["number"])
    print(f"Found {len(issues)} issues (topics). Fetching comments with {max_workers} workers ...")

    # Comments per issue are independent GETs -- safe to fetch concurrently,
    # bounded so we don't hammer the API even though the token has headroom.
    comments_by_num: dict[int, list[dict]] = {}
    with cf.ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {
            pool.submit(gh_api_paginated, f"repos/{repo}/issues/{i['number']}/comments?per_page=100"): i["number"]
            for i in issues
        }
        for fut in cf.as_completed(futures):
            num = futures[fut]
            comments_by_num[num] = fut.result()

    jobs: list[NoteJob] = []
    for issue in issues:
        num = issue["number"]
        title = issue["title"]
        topic_dir = out_dir / safe_dirname(title)

        issue_body = issue.get("body") or ""
        if issue_body.strip():
            note_title = derive_title(issue_body, title)
            jobs.append(NoteJob(
                created_at=issue.get("created_at", ""),
                topic_dir=topic_dir,
                note_title=note_title,
                body=issue_body,
                commit_label=f"{title}: {note_title}",
            ))

        comments = comments_by_num.get(num, [])
        print(f"  [Issue #{num}] {title}: {len(comments)} comments")
        for c in comments:
            body = c.get("body") or ""
            note_title = derive_title(body, f"note-{c['id']}")
            jobs.append(NoteJob(
                created_at=c.get("created_at", ""),
                topic_dir=topic_dir,
                note_title=note_title,
                body=body,
                commit_label=f"{title}: {note_title}",
            ))

    jobs.sort(key=lambda j: j.created_at or "")
    return jobs


def commit_note(repo_root: Path, paths: list[Path], created_at: str, message: str) -> bool:
    rel_paths = [str(p.relative_to(repo_root)) for p in paths]
    add = subprocess.run(["git", "add", "--"] + rel_paths, cwd=repo_root, capture_output=True, text=True)
    if add.returncode != 0:
        print(f"    ! git add failed: {add.stderr}", file=sys.stderr)
        return False
    env = os.environ.copy()
    if created_at:
        env["GIT_AUTHOR_DATE"] = created_at
        env["GIT_COMMITTER_DATE"] = created_at
    commit = subprocess.run(
        ["git", "commit", "--quiet", "-m", message],
        cwd=repo_root, capture_output=True, text=True, env=env,
    )
    if commit.returncode != 0:
        if "nothing to commit" in (commit.stdout + commit.stderr):
            return False
        print(f"    ! git commit failed: {commit.stderr}", file=sys.stderr)
        return False
    return True


def write_and_commit(jobs: list[NoteJob], repo_root: Path, do_commit: bool, image_cache: dict[str, bytes | None]):
    # Git operations are inherently sequential (shared index, and we need
    # commits in chronological order), so this loop stays single-threaded --
    # only the network fetching above was parallelized.
    for job in jobs:
        job.topic_dir.mkdir(parents=True, exist_ok=True)
        dt_prefix = (job.created_at[:19].replace(":", "-") if job.created_at else "0000-00-00")
        stem = f"{dt_prefix}_{slugify(job.note_title, 60)}"
        note_body = process_images(job.body, job.topic_dir, stem, image_cache)
        md_path = job.topic_dir / f"{stem}.md"
        # Avoid clobbering a distinct note that happens to slugify identically.
        n = 2
        while md_path.exists():
            md_path = job.topic_dir / f"{stem}-{n}.md"
            n += 1
        md_path.write_text(build_note_content(job.note_title, note_body), encoding="utf-8")
        print(f"  wrote {md_path.relative_to(repo_root)}")

        if do_commit:
            img_dir = job.topic_dir / f"{stem}_files"
            paths = [md_path] + ([img_dir] if img_dir.exists() else [])
            committed = commit_note(repo_root, paths, job.created_at, f"Add note: {job.commit_label}")
            if committed:
                print(f"    committed (dated {job.created_at})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--out", default=".", help="Output directory, relative to repo root")
    ap.add_argument("--issue", type=int, default=None, help="Only export a single issue number (for testing)")
    ap.add_argument("--no-commit", action="store_true", help="Write files only, skip git commits")
    ap.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help="Max concurrent network requests")
    args = ap.parse_args()

    repo_root = Path(
        subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
        or "."
    ).resolve()
    out_dir = (repo_root / args.out).resolve()

    jobs = collect_jobs(args.repo, out_dir, args.issue, args.workers)
    print(f"\nTotal notes to write: {len(jobs)}")
    image_cache = prefetch_images(jobs, args.workers)
    write_and_commit(jobs, repo_root, do_commit=not args.no_commit, image_cache=image_cache)
    print(f"\nDone. Exported to {out_dir}")


if __name__ == "__main__":
    main()
