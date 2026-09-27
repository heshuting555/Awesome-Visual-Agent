#!/usr/bin/env python3
"""Check catalogue completeness, identities, provenance, and generated Markdown."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))

def validate():
    papers, sections, meta = load('papers.json'), load('sections.json'), load('metadata.json')
    bib = (ROOT / 'references.bib').read_text(encoding='utf-8')
    bib_keys = {key.strip() for kind, key in re.findall(r'@([a-zA-Z]+)\s*\{\s*([^,]+),', bib) if kind.lower() not in {'comment', 'string', 'preamble', 'ieeetranbstctl'}}
    keys = [k for p in papers for k in p['citation_keys']]
    assert len(keys) == len(set(keys)), 'A BibTeX key is assigned to multiple works.'
    assert set(keys) == bib_keys, f'Bibliography mismatch: missing={bib_keys-set(keys)}, extra={set(keys)-bib_keys}'
    assert meta['bibliography_keys'] == len(bib_keys)
    assert meta['bibliography_sha256'] == hashlib.sha256((ROOT / 'references.bib').read_bytes()).hexdigest()
    mapping = load('source-map.json')['effective_sections_by_citation_key']
    assert set(mapping) == bib_keys, 'Effective section map does not cover the bibliography.'
    assert all(mapping[k] == p['sections'] for p in papers for k in p['citation_keys']), 'Effective section map disagrees with the catalogue.'
    assert len(papers) == meta['unique_works']
    assert sum(bool(p['arxiv_url']) for p in papers) == meta['arxiv_links']
    assert sum(bool(p['code_url']) for p in papers) == meta['code_links']
    section_ids = {s['id'] for s in sections}
    assert len(section_ids) == len(sections)
    for s in sections:
        assert s['parent'] is None or s['parent'] in section_ids
    arxiv = []
    for p in papers:
        assert p['title'].strip() and p['citation_keys'] and p['sections'], p['id']
        assert set(p['sections']) <= section_ids, p['id']
        assert all(a['section'] in section_ids for a in p['assignments']), p['id']
        assert all(a['citation_key'] in p['citation_keys'] for a in p['assignments']), p['id']
        for field in ('arxiv_url', 'code_url', 'paper_url', 'project_url'):
            u = p.get(field)
            if u:
                parts = urlsplit(u)
                assert parts.scheme in {'http', 'https'} and '.' in parts.netloc and not re.search(r'[\s<>]', u), (p['id'], field, u)
        for field in ('additional_code_urls', 'additional_project_urls'):
            for u in p.get(field, []):
                parts = urlsplit(u)
                assert parts.scheme in {'http', 'https'} and '.' in parts.netloc and not re.search(r'[\s<>]', u), (p['id'], field, u)
        if p['arxiv_url']:
            assert p['arxiv_status'].startswith('verified'), p['id']
            arxiv.append(p['arxiv_url'])
        if p['code_url']:
            assert p['source_urls'] and p['link_evidence'], p['id']
            assert p['code_status'].startswith('verified'), p['id']
    assert len(arxiv) == len(set(arxiv)), 'Verified arXiv aliases were not merged.'
    for path in [ROOT / 'README.md', *ROOT.glob('docs/**/*.md')]:
        text = path.read_text(encoding='utf-8')
        anchors = set(re.findall(r'<a id="([^"]+)"', text))
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith('#'):
                assert target[1:] in anchors, (str(path), target)
            elif not urlsplit(target).scheme:
                assert (path.parent / unquote(target.split('#')[0])).exists(), (str(path), target)
        for line in text.splitlines():
            if line.startswith('|'):
                # Table rows must preserve escaped bars in paper titles.
                assert len(line.split('|')) in {4, 6}, (str(path), line)
    print(f'PASS: {len(bib_keys)} keys → {len(papers)} works; {len(sections)} sections; bibliography, links, anchors and provenance consistent.')

if __name__ == '__main__':
    validate()
