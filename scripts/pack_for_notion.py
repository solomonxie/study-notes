#!/usr/bin/env python3
"""
Build a single flat folder containing every note + every local image it
references, downscale+recompress images to JPEG (screenshots don't need
full-res lossless PNG and Notion's zip cap makes this necessary), then
bin-pack into zip files that are each <= 5MB, keeping every note in the
same zip as the images it references.

Output goes to a sibling directory, ../<repo-name>-notion-import/, so it
never ends up inside the repo / git history.

Usage: venv/bin/python scripts/pack_for_notion.py  (or plain python3, no
deps beyond stdlib + macOS's built-in `sips`)
"""
import os
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXPORT_ROOT = REPO.parent / f'{REPO.name}-notion-import'
OUT = EXPORT_ROOT / 'flat-notes'
ZIPDIR = EXPORT_ROOT / 'zips'
LISTING = EXPORT_ROOT / 'file-listing.txt'

SKIP_DIRS = {'.git', '.obsidian', 'scripts', '__pycache__'}
MD_IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

ZIP_HARD_CAP = 5 * 1024 * 1024
PACK_TARGET = int(4.5 * 1024 * 1024)  # margin below the hard cap

MAX_DIM = 1600      # longest side, px
JPEG_QUALITY = 80


def iter_md_files():
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith('.md'):
                yield Path(dirpath) / fn


def unique_name(base, taken):
    if base not in taken:
        taken.add(base)
        return base
    stem, ext = os.path.splitext(base)
    i = 2
    while f'{stem}-{i}{ext}' in taken:
        i += 1
    new = f'{stem}-{i}{ext}'
    taken.add(new)
    return new


def shrink_to_jpeg(src, dst):
    subprocess.run(
        ['sips', '-Z', str(MAX_DIM), '-s', 'format', 'jpeg',
         '-s', 'formatOptions', str(JPEG_QUALITY), str(src), '--out', str(dst)],
        check=True, capture_output=True,
    )


def main():
    for d in (OUT, ZIPDIR):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    md_files = sorted(iter_md_files())

    taken_names = set()
    md_flat_name = {}
    img_flat_name = {}   # abs src path -> flat .jpg name
    md_images = {}

    for md in md_files:
        md_flat_name[md] = unique_name(md.name, taken_names)
        refs = []
        for m in MD_IMG_RE.finditer(md.read_text(encoding='utf-8')):
            url = m.group(2)
            if url.startswith('http://') or url.startswith('https://'):
                continue
            target = (md.parent / url).resolve()
            if target.is_file():
                refs.append(target)
        md_images[md] = refs

    for md in md_files:
        for img in md_images[md]:
            if img not in img_flat_name:
                jpg_base = os.path.splitext(img.name)[0] + '.jpg'
                img_flat_name[img] = unique_name(jpg_base, taken_names)

    for md in md_files:
        text = md.read_text(encoding='utf-8')
        def repl(m):
            alt, url = m.group(1), m.group(2)
            if url.startswith('http://') or url.startswith('https://'):
                return m.group(0)
            target = (md.parent / url).resolve()
            flat = img_flat_name.get(target)
            return f'![{alt}]({flat})' if flat else m.group(0)
        (OUT / md_flat_name[md]).write_text(MD_IMG_RE.sub(repl, text), encoding='utf-8')

    failed = []
    for i, (src, flat) in enumerate(img_flat_name.items(), 1):
        try:
            shrink_to_jpeg(src, OUT / flat)
        except subprocess.CalledProcessError:
            failed.append(src)
        if i % 300 == 0:
            print(f'  shrunk {i}/{len(img_flat_name)}')
    for src in failed:  # fallback: copy original, un-renamed extension
        flat = os.path.splitext(img_flat_name[src])[0] + src.suffix
        flat = unique_name(flat, taken_names)
        img_flat_name[src] = flat
        shutil.copy2(src, OUT / flat)

    entries = sorted(OUT.iterdir(), key=lambda p: p.stat().st_size, reverse=True)
    total = sum(p.stat().st_size for p in entries)
    with open(LISTING, 'w') as f:
        for p in entries:
            f.write(f'{p.stat().st_size:>10}  {p.name}\n')
        f.write(f'\nTOTAL: {total} bytes ({total / 1024 / 1024:.1f} MB) across {len(entries)} files\n')

    # union-find: a note + the images it references (and any other note
    # sharing one of those images) must land in the same zip.
    parent = {}
    def find(x):
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for md in md_files:
        parent.setdefault(md, md)
        for img in md_images[md]:
            parent.setdefault(img, img)
            union(md, img)

    groups = {}
    for md in md_files:
        g = groups.setdefault(find(md), {'files': [], 'size': 0})
        flat = md_flat_name[md]
        g['files'].append(flat)
        g['size'] += (OUT / flat).stat().st_size
    for src, flat in img_flat_name.items():
        g = groups.setdefault(find(src), {'files': [], 'size': 0})
        if flat not in g['files']:
            g['files'].append(flat)
            g['size'] += (OUT / flat).stat().st_size

    units = sorted(groups.values(), key=lambda g: g['size'], reverse=True)

    bins = []
    oversized = 0
    for u in units:
        if u['size'] > PACK_TARGET:
            oversized += 1
            bins.append({'size': u['size'], 'files': list(u['files'])})
            continue
        for b in bins:
            if b['size'] + u['size'] <= PACK_TARGET:
                b['size'] += u['size']
                b['files'].extend(u['files'])
                break
        else:
            bins.append({'size': u['size'], 'files': list(u['files'])})

    width = len(str(len(bins)))
    sizes = []
    for i, b in enumerate(bins, 1):
        zpath = ZIPDIR / f'notion-import-{i:0{width}d}.zip'
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as zf:
            for fn in b['files']:
                zf.write(OUT / fn, arcname=fn)
        sizes.append(zpath.stat().st_size)

    over_cap = sum(1 for s in sizes if s > ZIP_HARD_CAP)
    print(f'notes={len(md_files)} images={len(img_flat_name)} (failed_shrink={len(failed)}) '
          f'export_total={total/1024/1024:.0f}MB')
    print(f'zips={len(bins)} over_5MB_cap={over_cap} '
          f'min={min(sizes)/1024/1024:.2f}MB max={max(sizes)/1024/1024:.2f}MB avg={sum(sizes)/len(sizes)/1024/1024:.2f}MB')
    print(f'-> {ZIPDIR}')


if __name__ == '__main__':
    main()
