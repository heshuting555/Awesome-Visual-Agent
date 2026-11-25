#!/usr/bin/env python3
"""Validate the bibliography, catalogue data, and survey homepage."""
import re
from collections import Counter
from urllib.parse import unquote, urlsplit
from bibtex_utils import arxiv_id, bibliography_digest, norm, parse, tex_text, venue
from build_readme import ROOT, framework_catalogue, read


def markdown_anchors(content):
    explicit = re.findall(r'<a (?:id|name)="([^"]+)"', content)
    assert len(explicit) == len(set(explicit)), 'Duplicate explicit Markdown anchor'
    result, occurrences = set(explicit), Counter()
    for heading in re.findall(r'^#+\s+(.+)$', content, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        index = occurrences[slug]
        result.add(slug + ('-' + str(index) if index else ''))
        occurrences[slug] += 1
    return result


def validate_markdown():
    files = [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md']
    contents = {path: path.read_text(encoding='utf-8') for path in files}
    anchors = {path: markdown_anchors(content) for path, content in contents.items()}
    for path, content in contents.items():
        targets = re.findall(r'\]\(([^)]+)\)', content)
        targets += re.findall(r'\b(?:href|src)="([^"]+)"', content)
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            assert linked.exists(), (path.relative_to(ROOT), target, 'Missing local link target')
            if parsed.fragment and linked.suffix == '.md':
                assert unquote(parsed.fragment) in anchors.get(linked, set()), (path.relative_to(ROOT), target, 'Missing anchor')


def validate_homepage_tables():
    content = (ROOT / 'README.md').read_text(encoding='utf-8')
    sections = re.findall(r'^<details\b[^>]*>(.*?)^</details>', content, re.M | re.S)
    assert 0 < len(sections) == len(re.findall(r'^<details\b', content, re.M)), 'Incomplete homepage groups'
    for section in sections:
        summary = re.search(r'^<summary>.+\((\d+)\)</summary>$', section, re.M)
        assert summary, 'Missing entry count in homepage summary'
        rows = re.findall(r'^\| .+ \|$', section, re.M)
        assert len(rows) - 2 == int(summary[1]), ('Incorrect homepage entry count', summary[0])


def validate():
    papers, taxonomy, meta = read('papers.json'), read('taxonomy.json'), read('metadata.json')
    selection, curation, sources = read('selection.json'), read('curation.json'), read('source-map.json')
    entries, _, errors, recovered = parse(ROOT / 'references.bib')
    assert not errors and not recovered, (errors, recovered)
    entries = [e for e in entries if e['type'] != 'ieeetranbstctl']
    bib = {e['key']: e for e in entries}
    assert len(bib) == len(entries), 'Duplicate bibliography keys'
    ids = [p['id'] for p in papers]
    keys = [k for p in papers for k in p['citation_keys']]
    assert len(ids) == len(set(ids)) and len(keys) == len(set(keys))
    assert set(ids) == set(selection), 'Catalogue must match explicit selection'
    assert set(keys) <= set(bib), 'Selected key absent from bibliography'
    assert set(curation['decisions']) == set(bib), 'Every bibliography key needs a decision'
    selected_decisions = {k for k, d in curation['decisions'].items() if d['status'] == 'selected'}
    assert selected_decisions == set(keys)
    assert all(d.get('reason') and d['status'] in {'selected', 'bibliography_only'} for d in curation['decisions'].values())
    digest = bibliography_digest(ROOT / 'references.bib')
    assert meta['bibliography_sha256'] == taxonomy['validation']['catalogue_bibliography_sha256'] == digest
    assert meta['snapshot_date'] == curation['snapshot_date'] == sources['source_snapshot']
    branches, categories, topics, by_topic = framework_catalogue(papers, taxonomy)
    assert (len(branches), len(categories), len(topics)) == (2, 10, 35)
    assert next(b['id'] for b in branches if any(c['id'] == 'planning' for c in b['categories'])) == 'external'
    assert meta['organization'] == 'curated_vision_framework'
    expected_meta = {'unique_works': len(papers), 'topic_placements': len(papers), 'bibliography_keys': len(bib),
                     'selected_bibliography_keys': len(keys), 'bibliography_only_keys': len(bib) - len(keys),
                     'framework_branches': len(branches), 'framework_categories': len(categories), 'framework_topics': len(topics),
                     'arxiv_links': sum(bool(p.get('arxiv_url')) for p in papers),
                     'code_links': sum(bool(p.get('code_url') or p.get('additional_code_urls')) for p in papers)}
    for field, count in expected_meta.items():
        assert meta[field] == count, (field, meta[field], count)
    assert meta['year_counts'] == dict(Counter(p['year'] for p in papers))
    assert set(sources['citation_locations']) <= set(bib)
    assert not set(sources['unresolved_manuscript_citations']) & set(bib)
    assert set(sources['effective_sections_by_citation_key']) == set(keys)
    arxiv_urls = []
    for p in papers:
        key, choice = p['id'], selection[p['id']]
        e = bib[key]
        assert key in p['citation_keys']
        assert p['title'] == tex_text(e['fields']['title']), key
        assert not re.search(r'[{}$\\]', p['title']), (key, 'Unrendered TeX')
        assert p['year'] == tex_text(e['fields']['year']) and 2024 <= int(p['year']) <= int(meta['snapshot_date'][:4]), key
        assert p['venue'] == venue(e), key
        assert p['primary_topic'] == choice['primary_topic'] and p['vision_focus'] == choice['vision_focus'], key
        assert sources['assignment_evidence'][key] == p['assignments'], key
        assert p['selection_evidence']['basis'] and p['assignments'], key
        for k in p['citation_keys']:
            assert sources['effective_sections_by_citation_key'][k] == p['sections']
            assert curation['decisions'][k]['work_id'] == key
            assert arxiv_id(bib[k]) == arxiv_id(e) and norm(tex_text(bib[k]['fields']['title'])) == norm(p['title']), (key, 'Unrelated alias')
        for field in ('paper_url', 'arxiv_url', 'project_url', 'code_url', 'additional_code_urls', 'additional_project_urls'):
            values = p.get(field) or []
            if isinstance(values, str):
                values = [values]
            for url in values:
                parsed = urlsplit(url)
                assert parsed.scheme in {'http', 'https'} and '.' in parsed.netloc and not re.search(r'[\s<>]', url), (key, field, url)
        assert p.get('paper_url') or p.get('arxiv_url'), key
        if arxiv_id(e):
            assert p['arxiv_url'].endswith('/' + arxiv_id(e)), (key, 'arXiv identity mismatch')
        if p.get('arxiv_url'):
            arxiv_urls.append(p['arxiv_url'])
        if p.get('code_url'):
            assert p.get('link_evidence') and p.get('code_status'), key
    assert len(arxiv_urls) == len(set(arxiv_urls)), 'Duplicate arXiv works'
    for topic in topics:
        assert set(topic['selected_citation_keys']) == {p['id'] for p in by_topic[topic['id']]}
    validate_markdown()
    validate_homepage_tables()
    print(f'PASS: {len(papers)} selected works and {len(bib)} bibliography keys. Catalogue data, homepage table counts, links, and anchors are consistent.')


if __name__ == '__main__':
    validate()
