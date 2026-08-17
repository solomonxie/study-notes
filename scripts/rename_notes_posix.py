#!/usr/bin/env python3
"""
One-time rename pass: switch note filenames from

    YYYY-MM-DDTHH-MM-SS_<title>.md

to a POSIX-friendlier

    YYYYMMDDHHMMSS_<title>.md

The title portion keeps Unicode (Chinese text, emoji) but has ASCII
punctuation that's awkward in shells/filesystems either dropped or
turned into '-': spaces and bracket/separator chars
( )[]{}<>:;,/\\|*&#~^$% become '-' (runs collapse to one), while
backtick/quote/!/? are just dropped. Leading/trailing '-'/'.'/' ' are
stripped.

Each note's matching <old-stem>_files/ image folder is renamed to
match, and the note's own ![alt](old-stem_files/img.png) links are
rewritten to the new folder name.

Uses `git mv` so history follows the file. Run once, review the diff,
commit.
"""
import os
import re
import subprocess
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'.git', '.obsidian', 'scripts', '__pycache__'}

DT_RE = re.compile(r'^(\d{4})-(\d{2})-(\d{2})T(\d{2})-(\d{2})-(\d{2})_(.+)\.md$')
HYPHEN_SET = re.compile(r'[ \(\)\[\]\{\}<>:;,/\\|*&#~^$%]+')
DROP_SET = re.compile(r'[`\'"!?]')


def sanitize_title(text):
    text = unicodedata.normalize('NFC', text)
    text = HYPHEN_SET.sub('-', text)
    text = DROP_SET.sub('', text)
    text = re.sub(r'-{2,}', '-', text)
    text = text.strip('-. ')
    return text or 'untitled'


def iter_md_files():
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith('.md'):
                yield Path(dirpath) / fn


def build_plan():
    plan = []
    taken_per_dir = {}
    for md in sorted(iter_md_files()):
        m = DT_RE.match(md.name)
        if not m:
            continue
        Y, Mo, D, H, Mi, S, title = m.groups()
        new_dt = f'{Y}{Mo}{D}{H}{Mi}{S}'
        new_title = sanitize_title(title)
        new_name = f'{new_dt}_{new_title}.md'
        taken = taken_per_dir.setdefault(md.parent, set())
        base_dt, base_title = new_dt, new_title
        i = 2
        while new_name in taken:
            new_name = f'{base_dt}_{base_title}-{i}.md'
            i += 1
        taken.add(new_name)
        old_files_dir = md.parent / (md.stem + '_files')
        plan.append({
            'old_md': md,
            'new_md': md.parent / new_name,
            'old_files_dir': old_files_dir if old_files_dir.is_dir() else None,
            'new_files_dir': md.parent / (new_name[:-3] + '_files'),
        })
    return plan


def git_mv(src, dst):
    subprocess.run(['git', 'mv', str(src), str(dst)], check=True, cwd=REPO)


def main():
    plan = build_plan()
    print(f'{len(plan)} notes to rename')

    renamed_dirs = 0
    for item in plan:
        if item['old_md'] != item['new_md']:
            git_mv(item['old_md'], item['new_md'])
        if item['old_files_dir'] is not None and item['old_files_dir'] != item['new_files_dir']:
            git_mv(item['old_files_dir'], item['new_files_dir'])
            renamed_dirs += 1

    # rewrite image links inside notes whose _files folder got renamed
    rewritten = 0
    for item in plan:
        if item['old_files_dir'] is None or item['old_files_dir'] == item['new_files_dir']:
            continue
        old_dirname = item['old_files_dir'].name
        new_dirname = item['new_files_dir'].name
        md_path = item['new_md']
        text = md_path.read_text(encoding='utf-8')
        new_text = text.replace(old_dirname + '/', new_dirname + '/')
        if new_text != text:
            md_path.write_text(new_text, encoding='utf-8')
            rewritten += 1

    print(f'renamed {len(plan)} notes, {renamed_dirs} image folders, '
          f'rewrote links in {rewritten} notes')


if __name__ == '__main__':
    main()
