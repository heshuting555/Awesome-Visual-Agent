#!/usr/bin/env python3
"""Refresh the catalogue metadata from the bibliography and selected works."""
import json
from collections import Counter
from pathlib import Path
from bibtex_utils import bibliography_digest, parse

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def save(name, value):
    (ROOT / 'data' / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def framework_catalogue(papers, taxonomy):
    branches = taxonomy['branches']
    categories = [c for b in branches for c in b['categories']]
    topics = [t for c in categories for t in c['topics']]
    by_topic = {t['id']: [] for t in topics}
    assert len(by_topic) == len(topics)
    for p in papers:
        assert p['sections'] == [p['primary_topic']], p['id']
        assert p.get('vision_focus') and int(p['year']) >= 2024, p['id']
        by_topic[p['primary_topic']].append(p)
    return branches, categories, topics, by_topic


def update_metadata():
    papers, taxonomy, meta = read('papers.json'), read('taxonomy.json'), read('metadata.json')
    branches, categories, topics, _ = framework_catalogue(papers, taxonomy)
    entries, _, errors, _ = parse(ROOT / 'references.bib')
    assert not errors, errors
    keys = {e['key'] for e in entries if e['type'] != 'ieeetranbstctl'}
    selected_keys = {k for p in papers for k in p['citation_keys']}
    assert selected_keys <= keys
    arxiv_count = sum(bool(p.get('arxiv_url')) for p in papers)
    code_count = sum(bool(p.get('code_url') or p.get('additional_code_urls')) for p in papers)
    meta.update(unique_works=len(papers), topic_placements=len(papers), arxiv_links=arxiv_count,
                code_links=code_count, bibliography_keys=len(keys), selected_bibliography_keys=len(selected_keys),
                bibliography_only_keys=len(keys - selected_keys), organization='curated_vision_framework',
                bibliography_sha256=bibliography_digest(ROOT / 'references.bib'),
                framework_branches=len(branches), framework_categories=len(categories), framework_topics=len(topics),
                year_counts=dict(Counter(p['year'] for p in papers)))
    save('metadata.json', meta)
    print(f'Updated metadata for {len(papers)} selected works across {len(topics)} topics and {len(keys)} bibliography keys.')


if __name__ == '__main__':
    update_metadata()
