#!/usr/bin/env python3
"""Validate bibliography identities, Figure 1 placements, evidence, and Markdown."""
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bibtex_utils import entry_venue, norm, parse, tex_text
from build_readme import anchor, framework_catalogue, rows

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def arxiv_id(entry):
    fields = entry['fields']
    value = tex_text(fields.get('eprint', ''))
    match = re.search(r'\b(\d{4}\.\d{4,5})\b', value)
    if not match:
        value = ' '.join(tex_text(fields.get(field, '')) for field in ('journal', 'url', 'xxxurl', 'doi'))
        match = re.search(r'(?:arxiv(?:\.org/(?:abs|pdf)/|[\s:]+)|10\.48550/arxiv[.:])(\d{4}\.\d{4,5})', value, re.I)
    return match[1] if match else None


def venue(entry):
    result = entry_venue(entry)
    if result == 'Official Release' and (arxiv_id(entry) or tex_text(entry['fields'].get('archiveprefix', '')).lower() == 'arxiv'):
        result = 'arXiv'
    return result


def markdown_anchors(text):
    explicit = re.findall(r'<a id="([^"]+)"', text)
    assert len(explicit) == len(set(explicit)), 'Duplicate explicit Markdown anchor'
    result = set(explicit)
    counts = Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'<[^>]*>', '', heading).strip().lower()
        slug = re.sub(r'[^\w\s-]', '', slug).replace(' ', '-')
        suffix = counts[slug]
        result.add(slug + ('-' + str(suffix) if suffix else ''))
        counts[slug] += 1
    return result


def validate_markdown():
    paths = [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md', *ROOT.glob('docs/**/*.md')]
    anchor_map = {path: markdown_anchors(path.read_text(encoding='utf-8')) for path in paths}
    for path in paths:
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            parsed = urlsplit(target)
            if parsed.scheme:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            assert linked.exists(), (str(path.relative_to(ROOT)), target, 'Missing local link')
            if parsed.fragment and linked.suffix == '.md':
                assert unquote(parsed.fragment) in anchor_map.get(linked, set()), (str(path.relative_to(ROOT)), target, 'Missing anchor')
        width = None
        for line in text.splitlines():
            if not line.startswith('|'):
                width = None
                continue
            cells = re.split(r'(?<!\\)\|', line)
            if width is None:
                width = len(cells)
            assert len(cells) == width, (str(path.relative_to(ROOT)), 'Inconsistent table columns', line)


def validate():
    papers, taxonomy, meta = load('papers.json'), load('taxonomy.json'), load('metadata.json')
    sections, source_map = load('sections.json'), load('source-map.json')
    entries, _, errors, recovered = parse(ROOT / 'references.bib')
    assert not errors and not recovered, (errors, recovered)
    assert len(entries) == len({entry['key'] for entry in entries}), 'Duplicate BibTeX key'
    bibliography = {entry['key']: entry for entry in entries if entry['type'] != 'ieeetranbstctl'}
    keys = [key for paper in papers for key in paper['citation_keys']]
    assert len(keys) == len(set(keys)), 'A BibTeX key belongs to multiple works'
    assert set(keys) == set(bibliography), {'missing': sorted(set(bibliography) - set(keys)), 'extra': sorted(set(keys) - set(bibliography))}
    assert meta['bibliography_keys'] == len(bibliography)
    digest = hashlib.sha256((ROOT / 'references.bib').read_bytes()).hexdigest()
    assert meta['bibliography_sha256'] == digest
    assert taxonomy['validation'].get('catalogue_bibliography_sha256', taxonomy['validation']['source_bibliography_sha256']) == digest

    branches, categories, topics, by_topic, representatives = framework_catalogue(papers, taxonomy)
    assert [branch['id'] for branch in branches] == ['internal', 'external']
    assert [category['id'] for category in branches[0]['categories']] == ['perception', 'reasoning', 'world', 'evaluation', 'evolving']
    assert [category['id'] for category in branches[1]['categories']] == ['planning', 'memory', 'tools', 'verification', 'safety']
    assert len(branches) == 2 and len(categories) == 10 and len(topics) == 35
    reasoning = next(category for category in categories if category['id'] == 'reasoning')
    assert [topic['name'] for topic in reasoning['topics']] == ['Interleaved Multimodal Reasoning', 'Visually Grounded Reasoning', 'Tool-Augmented Visual Reasoning', 'Programmatic Visual Reasoning']
    assert all(len(topic['works']) in {8, 12} for topic in topics)
    assert Counter(len(topic['works']) for topic in topics) == {12: 31, 8: 4}
    representative_placements = sum(len(value) for value in representatives.values())
    representative_works = len({identifier for value in representatives.values() for identifier in value})
    assert representative_placements == 404 and representative_works == 261
    section_ids = {section['id'] for section in sections}
    assert len(section_ids) == len(sections) == len(branches) + len(categories) + len(topics)
    assert {section['id'] for section in sections if section['depth'] == 3} == {topic['id'] for topic in topics}
    assert all(section['parent'] is None or section['parent'] in section_ids for section in sections)
    assert meta['organization'] == 'figure1_framework'
    for field, value in {
        'unique_works': len(papers), 'framework_branches': len(branches),
        'framework_categories': len(categories), 'framework_topics': len(topics),
        'topic_placements': sum(len(paper['sections']) for paper in papers),
        'representative_works': representative_works, 'representative_topic_placements': representative_placements,
        'arxiv_links': sum(bool(paper.get('arxiv_url')) for paper in papers),
        'code_links': sum(bool(paper.get('code_url') or paper.get('additional_code_urls')) for paper in papers),
    }.items():
        assert meta[field] == value, (field, meta[field], value)
    assert meta['year_counts'] == dict(Counter(paper['year'] for paper in papers))
    assert meta['active_citation_keys'] == len(source_map['citation_locations'])
    assert meta['active_citation_keys'] + meta['provenance_only_keys'] == len(bibliography)
    assert set(source_map['citation_locations']) <= set(bibliography)
    assert meta['unresolved_manuscript_citation_keys'] == len(source_map.get('unresolved_manuscript_citations', {}))
    assert not set(source_map.get('unresolved_manuscript_citations', {})) & set(bibliography)
    mapping = source_map['effective_sections_by_citation_key']
    assert set(mapping) == set(bibliography)
    assert all(mapping[key] == paper['sections'] for paper in papers for key in paper['citation_keys'])

    historical_aliases = load('bibliography-update.json')['historical_import']['merged_title_variants']
    arxiv_urls = []
    for paper in papers:
        identifier = paper['id']
        assert identifier in paper['citation_keys'] and paper['title'].strip(), identifier
        assert not re.search(r'[{}$\\]', paper['title']), (identifier, 'Unrendered TeX title')
        assert paper['year'] == tex_text(bibliography[identifier]['fields']['year']), identifier
        assert paper['venue'] == venue(bibliography[identifier]), (identifier, paper['venue'], venue(bibliography[identifier]))
        assert {assignment['section'] for assignment in paper['assignments']} == set(paper['sections']), (identifier, 'Topic without assignment evidence')
        assert all(assignment['citation_key'] in paper['citation_keys'] for assignment in paper['assignments']), identifier
        assert source_map['assignment_evidence'][identifier] == paper['assignments'], identifier
        if len(paper['citation_keys']) > 1:
            identities = {arxiv_id(bibliography[key]) for key in paper['citation_keys']}
            titles = {norm(tex_text(bibliography[key]['fields']['title'])) for key in paper['citation_keys']}
            audited = any(set(record['citation_keys']) == set(paper['citation_keys'])
                          and record['arxiv_url'] == paper['arxiv_url']
                          and identities - {None} <= {record['arxiv_url'].rsplit('/', 1)[-1]}
                          and titles <= {norm(title) for title in record['titles']}
                          for record in historical_aliases)
            assert (len(identities) == 1 and None not in identities) or len(titles) == 1 or audited, (identifier, 'Unrelated bibliography aliases')
        for field in ('arxiv_url', 'paper_url', 'code_url', 'project_url', 'additional_code_urls', 'additional_project_urls'):
            values = paper.get(field) or []
            if isinstance(values, str):
                values = [values]
            for url in values:
                parsed = urlsplit(url)
                assert parsed.scheme in {'http', 'https'} and '.' in parsed.netloc and not re.search(r'[\s<>]', url), (identifier, field, url)
        if paper.get('arxiv_url'):
            assert paper['arxiv_status'].startswith('verified') or paper['arxiv_status'] == 'bibliography_supplied', identifier
            arxiv_urls.append(paper['arxiv_url'])
        if paper.get('code_url'):
            assert paper.get('source_urls') and paper.get('link_evidence'), identifier
            assert paper['code_status'].startswith('verified') or paper['code_status'] == 'bibliography_supplied', identifier
        if paper.get('classification_confidence'):
            assert paper['classification_confidence'] in {'high', 'medium', 'low'}
            assert paper['reference_role'] in {'method', 'benchmark', 'background'}
    assert len(arxiv_urls) == len(set(arxiv_urls)), 'arXiv aliases were not merged'

    validate_markdown()
    markdown = (ROOT / 'README.md').read_text(encoding='utf-8')
    actual_by_topic = defaultdict(list)
    current = None
    for line in markdown.splitlines():
        match = re.fullmatch(r'<a id="topic-([^"]+)"></a>', line)
        if match:
            current = match[1]
        elif line.startswith('<a id=') or line.startswith('## '):
            current = None
        elif re.match(r'^\| \d{4} \|', line):
            assert current, ('Paper row outside a topic', line)
            actual_by_topic[current].append(line)
    assert set(actual_by_topic) == {anchor('topic', topic['id']).removeprefix('topic-') for topic in topics}
    for topic in topics:
        expected = rows(by_topic[topic['id']], representatives[topic['id']]).splitlines()[2:]
        assert actual_by_topic[topic['id']] == expected, (topic['id'], 'Missing, duplicate, misplaced, or out-of-order paper row')
    expected_headings = []
    for branch in branches:
        expected_headings.append('## ' + branch['name'])
        for category in branch['categories']:
            expected_headings.append('### ' + category['name'])
            expected_headings += ['#### ' + topic['name'] for topic in category['topics']]
    actual_headings = [line for line in markdown.splitlines() if line in set(expected_headings)]
    assert actual_headings == expected_headings, 'README hierarchy does not follow Figure 1'
    assert '## 📅 ' not in markdown and 'year_then_venue' not in markdown
    print(f'PASS: {len(bibliography)} keys → {len(papers)} works; 2 branches / 10 categories / 35 topics; {meta["topic_placements"]} placements; {representative_works}/{representative_placements} Figure representatives. Bibliography, aliases, topic rows, links, anchors, and provenance are consistent.')


if __name__ == '__main__':
    validate()
