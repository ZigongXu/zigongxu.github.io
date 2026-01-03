#!/usr/bin/env python3
"""
Scan content/publications, parse each publication's front matter, and rename folders to the pattern:
  year-lastnameoffirstauthor-firsttwoWordsOfTitle-JournalAcronym

This script is idempotent and will skip folders that already match the pattern.
It attempts to resolve author last names from author slugs in `authors:`; if the slug is 'me' or a known slug with a YAML in data/authors/, it will read the `family` or `name.display` field.

Run from repository root: python3 scripts/rename_publications.py
"""
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB_DIR = ROOT / 'content' / 'publications'
DATA_AUTHORS = ROOT / 'data' / 'authors'

JOURNAL_MAP = {
    'The Astrophysical Journal Letters': 'ApJL',
    'The Astrophysical Journal': 'ApJ',
    'Astronomy & Astrophysics': 'AandA',
    'Geophysical Research Letters': 'GRL',
    'Science Advances': 'SciAdv',
    'Space Science Reviews': 'SSRv',
    'Monthly Notices of the Royal Astronomical Society': 'MNRAS',
    'Frontiers in Astronomy and Space Sciences': 'FrASS',
}

SKIP = {'_conference-paper', 'journal-article', 'preprint', '_index.md', 'cite.bib', 'public', 'publications'}

def read_front_matter(index_path: Path):
    text = index_path.read_text(encoding='utf8')
    m = re.search(r'^---\n(.*?)\n---', text, re.S | re.M)
    if not m:
        return {}
    body = m.group(1)
    data = {}
    # crude YAML parsing for keys we need
    # title
    t = re.search(r'^title:\s*"?(.*?)"?\s*$', body, re.M)
    if t:
        data['title'] = t.group(1).strip().strip('"')
    # date
    d = re.search(r'^date:\s*"?(.*?)"?\s*$', body, re.M)
    if d:
        data['date'] = d.group(1).strip()
    # publication or publication_short
    p = re.search(r'^publication_short:\s*"?(.*?)"?\s*$', body, re.M)
    if p and p.group(1).strip():
        data['publication_short'] = p.group(1).strip()
    else:
        p2 = re.search(r'^publication:\s*"?(.*?)"?\s*$', body, re.M)
        if p2:
            data['publication'] = p2.group(1).strip()
    # authors list
    a = re.search(r'^authors:\n((?:\s*- .*\n)+)', body, re.M)
    if a:
        lines = [ln.strip()[2:].strip() for ln in a.group(1).strip().splitlines()]
        data['authors'] = lines
    return data

def first_two_words(title: str):
    words = re.findall(r"[A-Za-z0-9]+", title)
    first = words[:2]
    return '-'.join(w.lower() for w in first)

def first_author_lastname(slug_or_name: str):
    # If slug contains hyphen assume slug is full-name; take last part
    if '-' in slug_or_name:
        return slug_or_name.split('-')[-1]
    # if slug is 'me' or other short form, try to read data/authors/<slug>.yaml
    candidate = DATA_AUTHORS / f"{slug_or_name}.yaml"
    if candidate.exists():
        txt = candidate.read_text(encoding='utf8')
        m = re.search(r'family:\s*"?(.*?)"?\s*$', txt, re.M)
        if m:
            return re.sub(r'\s+', '-', m.group(1).strip()).lower()
        m2 = re.search(r'name:\n\s*display:\s*"?(.*?)"?\s*$', txt, re.M)
        if m2:
            fam = m2.group(1).strip().split()[-1]
            return fam.lower()
    # fallback: use the slug as-is
    return slug_or_name.lower()

def journal_acronym(data):
    if 'publication_short' in data and data['publication_short']:
        return data['publication_short']
    if 'publication' in data:
        pub = data['publication']
        return JOURNAL_MAP.get(pub, ''.join(re.findall(r'[A-Za-z]', pub))[:6])
    return 'paper'

def make_new_slug(folder: Path, fm: dict):
    # derive year
    year = None
    if 'date' in fm and fm['date']:
        year = fm['date'][:4]
    else:
        # try folder name prefix
        m = re.match(r'(\d{4})', folder.name)
        if m:
            year = m.group(1)
    if not year:
        year = 'xxxx'
    # first author
    first_author = fm.get('authors', [None])[0]
    if not first_author:
        first_author = folder.name.split('-')[0]
    lastname = first_author_lastname(first_author)
    # first two words
    title = fm.get('title', folder.name)
    first2 = first_two_words(title)
    journal = journal_acronym(fm)
    slug = f"{year}-{lastname}-{first2}-{journal}"
    # sanitize: lower-case except journal we keep as-is, replace spaces
    slug = slug.replace(' ', '-').replace('--', '-')
    return slug

def main():
    planned = []
    for child in sorted(PUB_DIR.iterdir()):
        if child.name in SKIP or not child.is_dir():
            continue
        idx = child / 'index.md'
        if not idx.exists():
            continue
        fm = read_front_matter(idx)
        newslug = make_new_slug(child, fm)
        newpath = PUB_DIR / newslug
        if newpath.exists():
            # skip if exact same path exists
            if child.samefile(newpath):
                continue
            # prefer not to overwrite
            print(f"Target exists, skipping {child} -> {newpath}")
            continue
        planned.append((child, newpath))

    if not planned:
        print('No renames planned.')
        return

    print('Planned renames:')
    for src, dst in planned:
        print(f"  {src.name} -> {dst.name}")

    # proceed
    for src, dst in planned:
        print(f"Renaming {src} -> {dst}")
        shutil.move(str(src), str(dst))

    print('Done.')

if __name__ == '__main__':
    main()
