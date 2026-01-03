#!/usr/bin/env python3
"""
Generate publication pages and author YAMLs from content/publications/cite.bib

Naming conventions used:
 - publication folder: year-lastname-firsttwowords-journalAcronym (as requested)
 - author slug: given-family (lowercased, spaces->hyphen)

This script will skip entries that already have a folder present.

Run: python3 scripts/generate_publications_from_bib.py
"""
import re
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / 'content' / 'publications' / 'cite.bib'
OUT = ROOT / 'content' / 'publications'
AUTH = ROOT / 'data' / 'authors'

JOURNAL_MAP = {
    'apjl': 'ApJL',
    'apj': 'ApJ',
    'aap': 'AandA',
    'grl': 'GRL',
    'sciadv': 'SciAdv',
    'ssrv': 'SSRv',
    'mnras': 'MNRAS',
    'frass': 'FrASS'
}

def slugify(s: str) -> str:
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r"[^\w\s-]", '', s).strip().lower()
    s = re.sub(r"[\s_]+", '-', s)
    return s

def author_slug(given: str, family: str) -> str:
    g = slugify(given) if given else ''
    f = slugify(family) if family else ''
    if g:
        return f"{g}-{f}".strip('-')
    return f

def parse_bib(bib_text: str):
    entries = re.split(r'@', bib_text)
    parsed = []
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        m = re.match(r'(\w+)\{([^,]+),', entry)
        if not m:
            continue
        typ = m.group(1)
        key = m.group(2)
        # extract fields
        fields = dict(re.findall(r'([a-zA-Z_]+)\s*=\s*\{(.*?)\},', entry, re.S))
        # fallback fields with possible newlines
        title = fields.get('title', '').strip()
        authors = fields.get('author', '').strip()
        journal = fields.get('journal', '') or fields.get('journal', fields.get('booktitle', ''))
        year = fields.get('year', '')
        doi = fields.get('doi', '')
        eprint = fields.get('eprint', '')
        parsed.append({'key': key, 'type': typ, 'title': title, 'authors': authors, 'journal': journal, 'year': year, 'doi': doi, 'eprint': eprint})
    return parsed

def split_authors(auth_field: str):
    # authors separated by ' and '
    parts = [p.strip() for p in re.split(r'\s+and\s+', auth_field) if p.strip()]
    out = []
    for p in parts:
        # expected formats: {Lastname}, Given [M.]  OR Given Lastname
        p = p.strip()
        # remove outer braces
        p = p.strip('{}')
        if ',' in p:
            family, given = [x.strip() for x in p.split(',', 1)]
        else:
            pieces = p.split()
            family = pieces[-1]
            given = ' '.join(pieces[:-1])
        out.append({'given': given, 'family': family})
    return out

def journal_acronym(journal_field: str):
    if not journal_field:
        return 'paper'
    j = journal_field.lower()
    # try short mappings
    for k, v in JOURNAL_MAP.items():
        if k in j or k.upper() in journal_field:
            return v
    # fallback: take initials of words
    words = re.findall(r'[A-Za-z]+', journal_field)
    if len(words) <= 2:
        return ''.join(w.capitalize() for w in words)[:6]
    return ''.join(w[0].upper() for w in words[:3])

def make_folder_name(year, first_author_family, title, journal_acro):
    first2 = '-'.join(re.findall(r"[A-Za-z0-9]+", title)[:2]).lower()
    fam = slugify(first_author_family)
    return f"{year}-{fam}-{first2}-{journal_acro}"

def ensure_author_yaml(given, family):
    slug = author_slug(given, family)
    if not slug:
        slug = slugify(family)
    path = AUTH / f"{slug}.yaml"
    if path.exists():
        return slug
    display = f"{given} {family}".strip()
    content = f"schema: hugoblox/author/v1\nslug: {slug}\nname:\n  display: \"{display}\"\n  given: \"{given}\"\n  family: \"{family}\"\nrole: \"\"\nlinks: []\n"
    path.write_text(content, encoding='utf8')
    return slug

def generate():
    bib_text = BIB.read_text(encoding='utf8')
    entries = parse_bib(bib_text)
    created = 0
    for e in entries:
        # determine first author
        authors = split_authors(e['authors']) if e['authors'] else []
        if authors:
            first = authors[0]
        else:
            first = {'given': '', 'family': 'unknown'}
        year = e['year'] or 'xxxx'
        journal_acro = journal_acronym(e['journal'])
        folder = make_folder_name(year, first['family'], e['title'], journal_acro)
        outdir = OUT / folder
        if outdir.exists():
            continue
        # create author slugs and list
        author_slugs = []
        for a in authors:
            slug = ensure_author_yaml(a['given'], a['family'])
            author_slugs.append(slug)
        # write index.md
        outdir.mkdir(parents=True, exist_ok=True)
        doi = e['doi']
        arxiv = e['eprint']
        pub_name = e['journal'] or ''
        content = ['---']
        content.append(f'title: "{e["title"].strip()}"')
        content.append('authors:')
        for s in author_slugs:
            content.append(f'- {s}')
        content.append(f'date: "{year}-01-01T00:00:00Z"')
        content.append(f'publishDate: "{year}-01-01T00:00:00Z"')
        content.append('\npublication_types: ["article-journal"]')
        content.append(f'publication: "{pub_name}"')
        content.append(f'publication_short: "{journal_acro}"')
        content.append(f'\nsummary: """""')
        content.append('')
        content.append('tags:')
        content.append('  - auto-generated')
        content.append('\nfeatured: false')
        content.append('\n hugoblox:')
        content.append('  ids:')
        if doi:
            content.append(f'    doi: {doi}')
        if arxiv:
            content.append(f'    arxiv: {arxiv}')
        content.append('\nlinks:')
        if arxiv:
            content.append('  - type: preprint')
            content.append('    provider: arxiv')
            content.append(f'    id: {arxiv}')
        if doi:
            content.append('  - type: doi')
            content.append(f'    url: https://doi.org/{doi}')
        content.append('\nprojects: []')
        content.append('slides: ""')
        content.append('---')
        content.append('\nAuto-generated from cite.bib')
        outdir.joinpath('index.md').write_text('\n'.join(content), encoding='utf8')
        created += 1
    print(f'Created {created} publication pages')

if __name__ == '__main__':
    generate()
