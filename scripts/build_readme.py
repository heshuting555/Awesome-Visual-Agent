#!/usr/bin/env python3
"""Render the explicitly curated vision-agent reading list."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from bibtex_utils import parse

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def save(name, value):
    (ROOT / 'data' / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def cell(value):
    return (str(value if value is not None else '—').replace('|', '&#124;').replace('\n', ' ')
            .replace('<', '&lt;').replace('>', '&gt;').replace('[', '&#91;').replace(']', '&#93;'))


def anchor(kind, identifier):
    return kind + '-' + re.sub(r'[^a-z0-9_-]+', '-', identifier.lower()).strip('-')


def ordered(papers):
    return sorted(papers, key=lambda p: (-int(p['year']), p['title'].casefold(), p['id']))


def rows(papers):
    lines = ['| Year | Venue | Paper | Vision contribution | Project / Code |',
             '| :---: | :---: | --- | --- | :---: |']
    for p in ordered(papers):
        url = p.get('paper_url') or p.get('arxiv_url')
        assert url, (p['id'], 'Selected works need a paper link')
        title = '[' + cell(p['title']) + '](' + url + ')'
        if p.get('arxiv_url') and p['arxiv_url'] != url:
            title += ' · [arXiv](' + p['arxiv_url'] + ')'
        resources = []
        for label, field in [('Project', 'project_url'), ('Code', 'code_url')]:
            urls = list(dict.fromkeys(u for u in [p.get(field)] + p.get('additional_' + field + 's', []) if u))
            resources += ['[' + (label if len(urls) == 1 else label + ' ' + str(i + 1)) + '](' + u + ')'
                          for i, u in enumerate(urls)]
        lines.append('| ' + ' | '.join([cell(p['year']), cell(p['venue']), title,
                                       cell(p['vision_focus']), ' · '.join(resources) or '—']) + ' |')
    return '\n'.join(lines)


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


def navigation(branches, by_topic, prefix=''):
    lines = []
    for b in branches:
        lines.append('- [' + b['name'] + '](' + prefix + '#' + anchor('branch', b['id']) + ')')
        for c in b['categories']:
            lines.append('  - [' + c['name'] + '](' + prefix + '#' + anchor('category', c['id']) + ')')
            for t in c['topics']:
                lines.append('    - [' + t['name'] + '](' + prefix + '#' + anchor('topic', t['id'])
                             + ') — ' + str(len(by_topic[t['id']])) + ' papers')
    return lines


def render():
    papers, taxonomy, meta = read('papers.json'), read('taxonomy.json'), read('metadata.json')
    branches, categories, topics, by_topic = framework_catalogue(papers, taxonomy)
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
                bibliography_sha256=hashlib.sha256((ROOT / 'references.bib').read_bytes()).hexdigest(),
                framework_branches=len(branches), framework_categories=len(categories), framework_topics=len(topics),
                year_counts=dict(Counter(p['year'] for p in papers)))
    save('metadata.json', meta)
    main = ['# 🔍 Seeing the Horizon of Vision Agent: A Survey', '',
            '**Awesome Vision Agents** — a curated reading list of recent vision-centric agents, benchmarks, and code.', '',
            f'**{len(papers)} selected papers** · **2024–2026** · **{len(categories)} categories / {len(topics)} topics** · **{code_count} papers with code**', '',
            'An agent becomes vision-centric when visual observations shape what it inspects, reasons about, remembers, predicts, verifies, or does next. This collection emphasizes active image and video inspection, grounded GUI and robot actions, 3D reasoning, visual world models, and feedback from observed results.', '',
            '**Selection policy.** We select recent works from the survey bibliography for a concrete visual mechanism or a benchmark that directly tests visual agents. Recent publication alone is insufficient. General text-agent frameworks, historical foundations, standalone model primitives, and broad datasets do not automatically enter the reading list. [Selection criteria and decisions](docs/CURATION.md).', '',
            '**Reading the tables.** The **Vision contribution** column explains why each paper belongs here. Papers appear once under their main contribution and are ordered by year, newest first, then title. There are no star or importance rankings. Years and venues follow the bibliography, so a 2024 conference paper may have an earlier preprint. A dash means no project/code link is recorded.', '',
            '[📖 Survey bibliography](references.bib) · [📦 Selected catalogue](data/papers.json) · [🧭 Topic navigation](docs/TOPICS.md) · [🔎 Sources and verification](docs/COVERAGE.md)', '',
            f'Updated: **{meta["snapshot_date"]}**. The survey bibliography contains **{len(keys)} citation keys**; it also retains background references needed by the manuscript.', '',
            '## Suggested starting points', '',
            'These entry points illustrate different visual mechanisms; they are editorial reading suggestions.', '',
            '| Visual mechanism | Start here |', '| --- | --- |']
    by_id = {p['id']: p for p in papers}
    for label, key in [('Active visual search', 'u_vstar'), ('Visual GUI grounding', 'wu2026gui'),
                       ('Thinking with images', 'zheng2026deepeyes'), ('Executable visual reasoning', 'zhao2025pyvision'),
                       ('Visual world models for control', 'wd_dreamzero2026'), ('Original visual evidence as memory', 'han2026vista'),
                       ('Visual navigation with verified goals', 'shi2026navharnessgoals'), ('Checking observed action effects', 'zhang2026don'),
                       ('Visual-agent evaluation', 'koh2024visualwebarena')]:
        p = by_id.get(key)
        if p:
            main.append('| ' + label + ' | [' + cell(p.get('abbreviation') or p['title']) + ']('
                        + (p.get('paper_url') or p['arxiv_url']) + ') |')
    main += ['', '## 📚 Table of Contents', ''] + navigation(branches, by_topic)
    main += ['', '## 📑 Selected Papers', '',
             'The organization follows the survey’s two branches: internal visual capabilities and harness infrastructure. Planning and orchestration belong to the harness branch.', '']
    for b in branches:
        main += ['<a id="' + anchor('branch', b['id']) + '"></a>', '', '## ' + b['name'], '']
        for c in b['categories']:
            main += ['<a id="' + anchor('category', c['id']) + '"></a>', '', '### ' + c['name'], '']
            for t in c['topics']:
                main += ['<a id="' + anchor('topic', t['id']) + '"></a>', '', '#### ' + t['name'], '', rows(by_topic[t['id']]), '']
    main += ['## Contributing', '',
             'Suggest papers or corrections through [issues](https://github.com/heshuting555/Awesome-Vision-Agent/issues) or pull requests. Include the specific visual contribution and a primary source. See [CONTRIBUTING.md](CONTRIBUTING.md).', '',
             '## Acknowledgements', '',
             'Table presentation draws on [Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications); the original collection also drew on [Awesome-Agentic-MLLMs](https://github.com/HJYao00/Awesome-Agentic-MLLMs). Linked papers and software retain their respective authorship and licenses.', '',
             '## Citation', '', 'Use [references.bib](references.bib) to cite individual works. The survey citation will be added when its public bibliographic record is available.', '']
    (ROOT / 'README.md').write_text('\n'.join(main), encoding='utf-8')
    index = ['# Vision-agent topic navigation', '', '[← Selected catalogue](../README.md)', '',
             'The hierarchy follows the survey framework. Reading-list selections are maintained independently from manuscript examples; each selected work has one primary topic.', '']
    index += navigation(branches, by_topic, '../README.md')
    index += ['', '## Topic IDs', '', '| Topic ID | Category | Topic |', '| --- | --- | --- |']
    for c in categories:
        for t in c['topics']:
            index.append('| `' + t['id'] + '` | ' + c['name'] + ' | ' + t['name'] + ' |')
    (ROOT / 'docs/TOPICS.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    coverage = ['# Catalogue sources and verification', '', f'Bibliography snapshot: **{meta["snapshot_date"]}**.', '',
                '| Item | Count |', '| --- | ---: |', f'| Survey bibliography keys | {len(keys)} |',
                f'| Selected unique works | {len(papers)} |', f'| Selected citation keys | {len(selected_keys)} |',
                f'| Bibliography-only keys | {len(keys - selected_keys)} |', f'| Papers with arXiv links | {arxiv_count} |',
                f'| Papers with code links | {code_count} |', '', '## Sources', '',
                '- [references.bib](../references.bib) is an exact copy of the current manuscript’s `all_references.bib`.',
                '- [selection.json](../data/selection.json) records explicit inclusion, primary topics, and visual contributions.',
                '- [curation.json](../data/curation.json) accounts for every current bibliography key as selected or bibliography-only.',
                '- [papers.json](../data/papers.json) preserves primary links and their dated verification evidence.',
                '- [source-map.json](../data/source-map.json) records current manuscript citation locations and selection evidence.',
                '- [metadata.json](../data/metadata.json) records counts and the bibliography SHA-256.', '', '## Verification scope', '',
                'Newly checked official arXiv and publisher pages are dated in each record’s `link_evidence`. Earlier link checks retain their original dates. URLs copied from the bibliography use `bibliography_supplied`; they do not claim a fresh availability check. Code/project links are carried over only when the paper identity matches. Missing links remain blank.', '',
                'Visual contribution summaries are editorial descriptions supported by manuscript discussion, retained source evidence, and newly checked abstracts. Their source types remain distinct in the catalogue. Selection does not claim a complete new full-paper audit or a ranking.', '',
                '## Rebuild', '', '```sh', 'python3 scripts/build_readme.py', 'python3 scripts/validate_catalog.py', '```', '',
                'The validator checks bibliography identities, explicit inclusion, date bounds, coverage decisions, one-topic placement, visual summaries, metadata, and all local Markdown links and anchors. A bibliography update cannot automatically promote papers into the reading list.', '']
    unresolved = read('source-map.json').get('unresolved_manuscript_citations', {})
    if unresolved:
        coverage += ['## Manuscript citation gaps', '',
                     f'The current source scan found **{len(unresolved)} citation keys** absent from the supplied bibliography. '
                     'They remain recorded in [source-map.json](../data/source-map.json) and are not silently imported into the reading list.', '',
                     ', '.join('`' + key + '`' for key in sorted(unresolved)), '']
    (ROOT / 'docs/COVERAGE.md').write_text('\n'.join(coverage), encoding='utf-8')
    print(f'Rendered {len(papers)} selected works / {len(topics)} topics; {len(keys)} bibliography keys; code={code_count}.')


if __name__ == '__main__':
    render()
