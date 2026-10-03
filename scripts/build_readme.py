#!/usr/bin/env python3
"""Render the Figure 1 framework catalogue and preserve the old chapter archive."""
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from bibtex_utils import parse

ROOT = Path(__file__).resolve().parents[1]
ISSUES = 'https://github.com/heshuting555/Awesome-Vision-Agent/issues'
ARCHIVE_MARKER = '<!-- legacy-framework-archive -->'


def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def cell(value):
    return (str(value if value is not None else '—').replace('|', '&#124;')
            .replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')
            .replace('[', '&#91;').replace(']', '&#93;'))


def anchor(kind, identifier):
    return kind + '-' + re.sub(r'[^a-z0-9_-]+', '-', identifier.lower()).strip('-')


def unique_urls(primary, additional):
    return list(dict.fromkeys(url for url in [primary] + list(additional or []) if url))


def rows(papers, representative=None):
    """Figure representatives first; other works alphabetically by title."""
    representative = representative or {}
    ordered = sorted(papers, key=lambda paper: (
        0 if paper['id'] in representative else 1,
        representative.get(paper['id'], {}).get('order', 0),
        paper['title'].casefold(), paper['id']))
    lines = ['| Year | Venue | Paper Abbr | Paper Title | Project/Code |',
             '| :---: | :---: | :---: | --- | :---: |']
    for paper in ordered:
        url = (paper.get('paper_url') or paper.get('arxiv_url')
               or paper.get('project_url') or paper.get('code_url'))
        title = '[' + cell(paper['title']) + '](' + url + ')' if url else cell(paper['title'])
        if paper.get('arxiv_url') and paper['arxiv_url'] != url:
            title += ' · [arXiv](' + paper['arxiv_url'] + ')'
        resources = []
        for label, urls in [
            ('Project', unique_urls(paper.get('project_url'), paper.get('additional_project_urls'))),
            ('Code', unique_urls(paper.get('code_url'), paper.get('additional_code_urls'))),
        ]:
            resources += ['[' + (label if len(urls) == 1 else label + ' ' + str(index + 1))
                          + '](' + url + ')' for index, url in enumerate(urls)]
        resource_cell = ' · '.join(resources) or (
            'Unavailable' if paper.get('code_status') == 'official_link_unavailable' else '—')
        abbr = paper.get('abbreviation') or '—'
        if paper['id'] in representative:
            abbr = '★ ' + representative[paper['id']].get('display_name', abbr)
        lines.append('| ' + ' | '.join([
            cell(paper.get('year')), cell(paper.get('venue')), cell(abbr), title, resource_cell]) + ' |')
    return '\n'.join(lines)


def framework_catalogue(papers, taxonomy):
    """Validate topic assignments and join Figure citation keys to catalogue identities."""
    branches = taxonomy['branches']
    categories = [category for branch in branches for category in branch['categories']]
    topics = [topic for category in categories for topic in category['topics']]
    assert len({branch['id'] for branch in branches}) == len(branches), 'Duplicate branch IDs'
    assert len({category['id'] for category in categories}) == len(categories), 'Duplicate category IDs'
    assert len({topic['id'] for topic in topics}) == len(topics), 'Duplicate topic IDs'
    topic_ids = {topic['id'] for topic in topics}
    assert len({paper['id'] for paper in papers}) == len(papers), 'Duplicate work identities'
    by_key = {}
    by_topic = {topic['id']: [] for topic in topics}
    for paper in papers:
        sections = paper.get('sections', [])
        assert sections and len(sections) == len(set(sections)), (paper['id'], 'Missing or duplicate topics')
        assert set(sections) <= topic_ids, (paper['id'], 'Unknown topic', set(sections) - topic_ids)
        assert paper['primary_topic'] in sections, (paper['id'], 'Invalid primary_topic')
        assert set(paper.get('representative_topics', [])) <= set(sections), paper['id']
        for key in paper['citation_keys']:
            assert key not in by_key, ('Citation key assigned to two works', key)
            by_key[key] = paper
        for section in sections:
            by_topic[section].append(paper)
        for assignment in paper.get('assignments', []):
            assert assignment['section'] in sections, (paper['id'], assignment)
            assert all(assignment.get(field) for field in ('source', 'classification', 'citation_key')), assignment
    representatives = {}
    expected_representative_topics = defaultdict(set)
    for topic in topics:
        current = {}
        for index, work in enumerate(topic['works']):
            key = work['citation_key']
            assert key in by_key, ('Figure representative absent from papers.json', key)
            paper = by_key[key]
            assert topic['id'] in paper['sections'], (key, topic['id'], 'Representative lacks placement')
            assert paper['id'] not in current, (key, topic['id'], 'Duplicate representative identity')
            current[paper['id']] = dict(work, order=index + 1)
            expected_representative_topics[paper['id']].add(topic['id'])
        representatives[topic['id']] = current
    for paper in papers:
        assert set(paper.get('representative_topics', [])) == expected_representative_topics[paper['id']], (
            paper['id'], 'Representative topic flags differ from Figure 1')
    return branches, categories, topics, by_topic, representatives


def navigation(branches, by_topic, prefix=''):
    lines = []
    for branch in branches:
        lines.append('- [' + branch['name'] + '](' + prefix + '#' + anchor('branch', branch['id']) + ')')
        for category in branch['categories']:
            lines.append('  - [' + category['name'] + '](' + prefix + '#' + anchor('category', category['id']) + ')')
            for topic in category['topics']:
                lines.append('    - [' + topic['name'] + '](' + prefix + '#' + anchor('topic', topic['id'])
                             + ') — ' + str(len(by_topic[topic['id']])) + ' works')
    return lines


def mark_legacy_archive():
    """Add a notice without regenerating or removing archived chapter content."""
    chapters = ROOT / 'docs/chapters'
    archives = sorted(chapters.glob('*.md')) if chapters.exists() else []
    for path in archives:
        content = path.read_text(encoding='utf-8')
        if ARCHIVE_MARKER not in content:
            notice = (ARCHIVE_MARKER + '\n'
                      '> **Legacy manuscript chapter archive.** These historical section assignments '
                      'reflect an earlier survey draft. For the current Figure 1 classification, use '
                      '[framework navigation](../TOPICS.md) or the [main catalogue](../../README.md).\n\n')
            path.write_text(notice + content, encoding='utf-8')
    return archives


def render():
    papers, taxonomy, meta = read('papers.json'), read('taxonomy.json'), read('metadata.json')
    branches, categories, topics, by_topic, representatives = framework_catalogue(papers, taxonomy)
    entries, _, errors, _ = parse(ROOT / 'references.bib')
    assert not errors, errors
    keys = {entry['key'] for entry in entries if entry['type'] != 'ieeetranbstctl'}
    catalogue_keys = {key for paper in papers for key in paper['citation_keys']}
    assert keys == catalogue_keys, {'missing_from_catalogue': sorted(keys - catalogue_keys),
                                    'missing_from_bibliography': sorted(catalogue_keys - keys)}
    arxiv_count = sum(bool(paper.get('arxiv_url')) for paper in papers)
    code_count = sum(bool(paper.get('code_url') or paper.get('additional_code_urls')) for paper in papers)
    placements = sum(len(paper['sections']) for paper in papers)
    representative_placements = sum(len(value) for value in representatives.values())
    representative_unique = len({identifier for value in representatives.values() for identifier in value})
    meta.update(unique_works=len(papers), topic_placements=placements, arxiv_links=arxiv_count,
                code_links=code_count, bibliography_keys=len(keys), organization='figure1_framework',
                bibliography_sha256=hashlib.sha256((ROOT / 'references.bib').read_bytes()).hexdigest(),
                framework_branches=len(branches), framework_categories=len(categories),
                framework_topics=len(topics), representative_works=representative_unique,
                representative_topic_placements=representative_placements)
    (ROOT / 'data/metadata.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    main = [
        '# 🔍 Seeing the Horizon of Vision Agent: A Survey', '',
        '**Awesome Vision Agents** — papers, benchmarks, projects, and code.', '',
        f'**{len(papers)} unique works** · **{placements} topic placements** · **{arxiv_count} arXiv links** '
        f'· **{code_count} works with code links** · **{len(keys)} BibTeX keys**', '',
        '💡 Welcome! This collection accompanies our survey on vision agents. It covers visual perception and reasoning, agent harnesses, memory, capability evolution, GUI and embodied applications, and evaluation.', '',
        '📌 Corrections and additions are welcome through [issues](' + ISSUES + ') or pull requests. See the [contribution guide](CONTRIBUTING.md).', '',
        '[📖 Full bibliography](references.bib) · [📦 Machine-readable catalogue](data/papers.json) '
        '· [🧭 Framework taxonomy](data/taxonomy.json) · [🔎 Coverage and provenance](docs/COVERAGE.md) '
        '· [🗂 Framework navigation](docs/TOPICS.md)', '',
        '## Introduction', '',
        f'Papers follow the latest **Figure 1 framework**: **{len(branches)} branches, {len(categories)} categories, '
        f'and {len(topics)} topics**. Internal capabilities cover perception, reasoning, world simulation, evaluation '
        'and correction, and evolution. The harness branch covers planning and orchestration, memory, visual tools, '
        'verification, and safety. Planning and orchestration are part of the harness.', '',
        '**Reading the tables.** ★ marks a representative work selected for that topic in Figure 1; these works '
        'appear first in the figure’s order. Other works are ordered alphabetically by title. A work may appear '
        'in several topics when its mechanisms support several parts of the framework; it appears once within '
        'each topic. Unique-work counts merge aliases, while topic-placement counts include these cross-listings. '
        'Year and venue remain descriptive table fields. A dash (—) means a name or link has not been identified. '
        'Project pages remain separate from code repositories, and evidence and verification dates are retained '
        'in the catalogue.', '',
        f'Bibliography snapshot: **{meta["snapshot_date"]}**. Classification sources and limits are documented '
        'in [coverage notes](docs/COVERAGE.md).', '',
        '## 📚 Table of Contents', '',
    ]
    main += navigation(branches, by_topic)
    main += ['', '## 📑 Paper List', '']
    for branch in branches:
        main += ['<a id="' + anchor('branch', branch['id']) + '"></a>', '', '## ' + branch['name'], '']
        for category in branch['categories']:
            main += ['<a id="' + anchor('category', category['id']) + '"></a>', '', '### ' + category['name'], '']
            for topic in category['topics']:
                items = by_topic[topic['id']]
                main += ['<a id="' + anchor('topic', topic['id']) + '"></a>', '', '#### ' + topic['name'], '',
                         f'{len(items)} works · {len(representatives[topic["id"]])} Figure 1 representatives.', '',
                         rows(items, representatives[topic['id']]), '']
    main += ['## 🙏 Acknowledgements', '',
             'The table presentation is inspired by [Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications). '
             'The earlier topic archive also drew on [Awesome-Agentic-MLLMs](https://github.com/HJYao00/Awesome-Agentic-MLLMs). '
             'Linked papers and software retain their respective authorship and licenses.', '',
             '## 📝 Citation', '',
             'Use [references.bib](references.bib) to cite the individual works. A citation for the survey will be '
             'added when its public bibliographic record is available.', '']
    (ROOT / 'README.md').write_text('\n'.join(main), encoding='utf-8')
    (ROOT / 'docs').mkdir(exist_ok=True)
    archives = mark_legacy_archive()
    topic_index = ['# Figure 1 framework navigation', '', '[← Main catalogue](../README.md)', '',
                   'This navigation follows the current Figure 1. Topic IDs come from its section labels; '
                   'the exact hierarchy and representative selections are recorded in [taxonomy.json](../data/taxonomy.json). '
                   'Each link opens the corresponding topic table in the README.', '']
    topic_index += navigation(branches, by_topic, '../README.md')
    topic_index += ['', '## Topic IDs for contributors', '', '| Topic ID | Branch | Category | Topic |',
                    '| --- | --- | --- | --- |']
    for branch in branches:
        for category in branch['categories']:
            for topic in category['topics']:
                topic_index.append('| `' + topic['id'] + '` | ' + cell(branch['name']) + ' | '
                                   + cell(category['name']) + ' | ' + cell(topic['name']) + ' |')
    if archives:
        topic_index += ['', '## Legacy manuscript chapter archive', '',
                        'These files preserve an earlier draft’s section assignments and historical evidence. '
                        'They are not the current catalogue classification.', '']
        topic_index += ['- [' + path.stem + '](chapters/' + path.name + ')' for path in archives]
    (ROOT / 'docs/TOPICS.md').write_text('\n'.join(topic_index) + '\n', encoding='utf-8')

    classification_counts = Counter()
    classification_works = defaultdict(set)
    for paper in papers:
        for assignment in paper.get('assignments', []):
            method = assignment['classification']
            classification_counts[method] += 1
            classification_works[method].add(paper['id'])
    no_paper_link = [paper for paper in papers if not paper.get('paper_url') and not paper.get('arxiv_url')]
    no_code_link = [paper for paper in papers if not paper.get('code_url') and not paper.get('additional_code_urls')]
    coverage = ['# Catalogue coverage and provenance', '',
                f'Bibliography snapshot: **{meta["snapshot_date"]}**. Original catalogue assembled: '
                f'**{meta.get("assembled_at", "not recorded")}**. Historical link evidence retains its original dates.', '',
                '| Item | Count |', '| --- | ---: |',
                f'| Bibliographic keys | {len(keys)} |',
                f'| Non-paper BibTeX control records (excluded) | {sum(entry["type"] == "ieeetranbstctl" for entry in entries)} |',
                f'| Unique works after merging aliases | {len(papers)} |',
                f'| Topic placements (cross-listings included) | {placements} |',
                f'| Framework branches / categories / topics | {len(branches)} / {len(categories)} / {len(topics)} |',
                f'| Figure 1 representative works (unique) | {representative_unique} |',
                f'| Figure 1 representative topic placements | {representative_placements} |',
                f'| Works with an arXiv link | {arxiv_count} |',
                f'| Works with code links | {code_count} |',
                f'| Works without an identified paper or arXiv link | {len(no_paper_link)} |',
                f'| Works without an identified code link | {len(no_code_link)} |', '',
                '## Data sources and reproducible coverage', '',
                '- [references.bib](../references.bib) is the unified bibliography; bibliography controls are excluded from paper counts.',
                '- [data/taxonomy.json](../data/taxonomy.json) records the current Figure 1 hierarchy, section labels, ordered topics, and representative citation keys.',
                '- [data/papers.json](../data/papers.json) records unique works, current citation keys, topic assignments, and preserved paper/project/code evidence.',
                '- [data/source-map.json](../data/source-map.json) retains manuscript citation positions and filenames without publishing manuscript prose.',
                '- [data/bibliography-update.json](../data/bibliography-update.json) retains bibliography imports, identity corrections, and alias migrations.',
                '- [data/metadata.json](../data/metadata.json) records counts, snapshot dates, and the bibliography SHA-256.', '',
                'The renderer checks that every bibliography key belongs to a catalogue work, every work has a valid '
                'framework topic and primary topic, and each Figure 1 representative is present in its topic. '
                'Cross-listing does not increase the unique-work count. Rebuild with `python3 scripts/build_readme.py` '
                'and validate with `python3 scripts/validate_catalog.py`.', '',
                '## Classification basis', '',
                'The hierarchy follows Figure 1, including planning and orchestration under harness infrastructure. '
                'Representative selections are explicitly identified by the figure. Other placements retain their '
                'assignment source and classification method in `papers.json`. A citation in a current manuscript '
                'subsection supports that placement; a mapping from an earlier draft preserves a historical topic '
                'basis; a title or bibliography-based classification is a curation inference and does not imply '
                'full-paper verification. These evidence types are kept distinct. Assignments can cross-list '
                'the same work when several mechanisms apply.', '',
                '| Recorded classification method | Assignment records | Unique works supported |',
                '| --- | ---: | ---: |']
    for method in sorted(classification_counts):
        coverage.append('| `' + cell(method) + '` | ' + str(classification_counts[method]) + ' | '
                        + str(len(classification_works[method])) + ' |')
    coverage += ['', 'Assignment-record counts may exceed topic placements when several sources support the '
                 'same work/topic pair. `legacy_sections` and `legacy_assignments` preserve old section evidence; '
                 'the [legacy chapter archive](TOPICS.md#legacy-manuscript-chapter-archive) remains available '
                 'without defining the current main grouping.', '',
                 '## Identity corrections and aliases', '',
                 'Current citation keys and historical aliases remain attached to catalogue identities. '
                 'A verified preprint/published pair appears as one work; current BibTeX keys remain available '
                 'in the bibliography. The historical key `chen2026reflect` was used for Reflect-R1 '
                 '(arXiv:2606.27922); the current bibliography uses it for Reflect, Revise, Reuse '
                 '(arXiv:2609.17653). Reflect-R1 is recorded separately under `chen2026reflectr1`.', '',
                 '| Work | Current citation keys |', '| --- | --- |']
    for paper in sorted(papers, key=lambda paper: (paper['title'].casefold(), paper['id'])):
        if len(paper['citation_keys']) > 1:
            coverage.append('| ' + cell(paper['title']) + ' | '
                            + ', '.join('`' + key + '`' for key in paper['citation_keys']) + ' |')
    coverage += ['', '## Verification scope', '',
                 'Bibliography syntax, duplicate keys, catalogue coverage, and framework membership are checked '
                 'during the update. Paper metadata and previously verified links retain their supporting '
                 'sources and dates. These checks do not mean that every full paper, venue/year label, or '
                 'repository has been independently re-audited.', '',
                 'An author-supplied code URL uses `verified_author_supplied_link`; it does not claim a fresh '
                 'repository availability check. Existing repository checks retain their original dates. '
                 'New URLs copied directly from the unified bibliography use `bibliography_supplied`; '
                 'this records their source and does not claim a fresh availability or identity check. '
                 'Missing links remain curation items, and a working link does not establish reproducibility.', '',
                 '## Paper links still to identify', '', rows(no_paper_link), '', '<details>',
                 '<summary>Code links still to identify</summary>', '', rows(no_code_link), '', '</details>', '']
    (ROOT / 'docs/COVERAGE.md').write_text('\n'.join(coverage), encoding='utf-8')
    print(f'Rendered {len(papers)} unique works across {placements} placements in {len(topics)} framework topics; '
          f'Figure representatives={representative_unique}/{representative_placements}, arXiv={arxiv_count}, code={code_count}.')


if __name__ == '__main__':
    render()
