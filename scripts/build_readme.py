#!/usr/bin/env python3
"""Render README and chapter pages from the public catalogue (Python 3.9+)."""
import json
import hashlib
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))

def cell(s):
    return str(s).replace('|', '&#124;').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')

def anchor(s):
    return 'section-' + s.replace('.', '-')

def rows(papers):
    out = ['| Year | Title | Paper | Code |', '| :---: | --- | :---: | :---: |']
    for p in sorted(papers, key=lambda p: (-int(p['year'] or 0), p['title'].casefold())):
        paper = []
        if p.get('arxiv_url'):
            paper.append('[arXiv](' + p['arxiv_url'] + ')')
        if p.get('paper_url') and p['paper_url'] != p.get('arxiv_url'):
            paper.append('[Paper](' + p['paper_url'] + ')')
        if p.get('project_url'):
            paper.append('[Project](' + p['project_url'] + ')')
        codes = ([p['code_url']] if p.get('code_url') else []) + p.get('additional_code_urls', [])
        code = ' · '.join('[' + (u.rstrip('/').rsplit('/', 1)[-1] if len(codes) > 1 else 'Code') + '](' + u + ')' for u in codes) or ('Unavailable' if p.get('code_status') == 'official_link_unavailable' else '—')
        out.append('| ' + ' | '.join([cell(p['year']), cell(p['title']), ' · '.join(paper) or '—', code]) + ' |')
    return '\n'.join(out)

def render():
    papers = read('papers.json')
    sections = read('sections.json')
    meta = read('metadata.json')
    by_section = {s['id']: [p for p in papers if s['id'] in p['sections']] for s in sections}
    top = [s for s in sections if s['depth'] == 1]
    nc = sum(bool(p['code_url']) for p in papers)
    na = sum(bool(p['arxiv_url']) for p in papers)
    bib = (ROOT / 'references.bib').read_bytes()
    bib_keys = {key.strip() for kind, key in re.findall(r'@([a-zA-Z]+)\s*\{\s*([^,]+),', bib.decode('utf-8')) if kind.lower() not in {'comment', 'string', 'preamble', 'ieeetranbstctl'}}
    meta.update(unique_works=len(papers), arxiv_links=na, code_links=nc, bibliography_keys=len(bib_keys), bibliography_sha256=hashlib.sha256(bib).hexdigest())
    (ROOT / 'data' / 'metadata.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    main = [
        '# Awesome Vision Agents', '',
        '**Seeing the Horizon of Vision Agent: A Survey**', '',
        'A collection of papers, code, and benchmarks on vision agents, organized by the chapters and subsections of our survey.', '',
        f'**{len(papers)} unique works** · **{na} arXiv entries** · **{nc} works with code** · **{meta["bibliography_keys"]} BibTeX keys**', '',
        '## Overview', '',
        'The collection covers the foundations of vision agents, runtime harnesses, capability acquisition and evolution, applications, evaluation, and open challenges. Section 3 follows the latest paradigm-based organization of visual evidence acquisition, visual memory, and grounded reasoning and planning.', '',
        '**How to read the tables.** Years follow the bibliography, except for primary-source corrections recorded in the catalogue; arXiv versions may have an earlier date. A dash (—) means that a link has not been identified and verified for this catalogue; it does not mean that a paper or implementation does not exist. Code links come from the paper, its author project, or a repository that identifies the paper. “Unavailable” marks an author-linked repository that could not be accessed at the snapshot date. The same work can appear in several relevant sections; duplicate BibTeX keys are merged in each table.', '',
        '[Full bibliography](references.bib) · [Machine-readable catalogue](data/papers.json) · [Coverage and provenance](docs/COVERAGE.md) · [Contributing](CONTRIBUTING.md)', '',
        '## Table of Contents', ''
    ]
    for s in sections:
        if s['depth'] <= 2:
            main.append('  ' * (s['depth'] - 1) + '- [' + s['id'] + '. ' + s['title'] + '](#' + anchor(s['id']) + ')')
    main += ['', '## Paper List', '']
    for chapter in top:
        sid = chapter['id']
        children = [s for s in sections if s['id'] == sid or s['id'].startswith(sid + '.')]
        chapter_lines = ['# ' + sid + '. ' + chapter['title'], '', '[← Main catalogue](../../README.md)', '']
        for s in children:
            heading = ('##' if s['depth'] == 1 else '###' if s['depth'] == 2 else '####') + ' ' + s['id'] + '. ' + s['title']
            block = ['<a id="' + anchor(s['id']) + '"></a>', '', heading, '']
            items = by_section[s['id']]
            if items:
                block += [rows(items), '']
            elif not any(by_section[t['id']] for t in sections if t['id'].startswith(s['id'] + '.')):
                block += ['References for this framing section are listed under their relevant topics in the catalogue.', '']
            main += block
            chapter_lines += block
        (ROOT / 'docs' / 'chapters' / (sid + '.md')).write_text('\n'.join(chapter_lines), encoding='utf-8')
    main += [
        '## Acknowledgements', '',
        'The hierarchical table-of-contents and paper-table presentation is inspired by [Awesome-Agentic-MLLMs](https://github.com/HJYao00/Awesome-Agentic-MLLMs). The categories and bibliography here follow our own survey. Linked papers and software retain their respective authorship and licenses.', '',
        '## Citation', '',
        'Use [references.bib](references.bib) to cite the individual works. A citation for the survey will be added when its public bibliographic record is available.', ''
    ]
    (ROOT / 'README.md').write_text('\n'.join(main), encoding='utf-8')
    coverage = [
        '# Catalogue coverage and provenance', '',
        f'Bibliography snapshot: **{meta["snapshot_date"]}**. Catalogue assembled: **{meta.get("assembled_at", meta["snapshot_date"])}**. Individual link-check dates are retained in the evidence.', '',
        '| Item | Count |', '| --- | ---: |',
        f'| Bibliographic keys | {meta["bibliography_keys"]} |',
        f'| Non-paper BibTeX control records (excluded) | {meta["nonpaper_records"]} |',
        f'| Unique works after merging aliases | {len(papers)} |',
        f'| Works with an arXiv link | {na} |',
        f'| Works with a verified code link | {nc} |',
        f'| Works without an identified arXiv link | {len(papers)-na} |',
        f'| Works without a verified code link | {len(papers)-nc} |', '',
        '## Organization', '',
        'The chapter and subsection names follow the manuscript input graph, with the latest separate revisions of Sections 3.1–3.3. Dormant manuscript fragments do not create new numbered sections. Figure citations can be placed under their corresponding harness topic. References not cited in the active manuscript are retained under the relevant chapter using their bibliography source or an explicitly recorded topical assignment; this is not evidence that the manuscript cites them in that section.', '',
        'Each record in [papers.json](../data/papers.json) preserves all citation-key aliases, section assignments and their basis, source URLs, and link status. [sections.json](../data/sections.json) lists the exact hierarchy. [source-map.json](../data/source-map.json) records source-file identifiers and mapping evidence. The additional-reference appendix holds work whose place in the main chapter taxonomy is not yet established. No unpublished manuscript body is bundled here.', '',
        '## Links', '',
        'arXiv identities were checked against primary-source titles; documented title variants were checked separately. Code links require an author-supplied link from a paper/project page or repository evidence identifying that paper. Project pages and model pages are not silently relabeled as code. A working URL alone does not establish paper identity. Repository identity checks do not verify that every experiment is reproducible.', '',
        'Missing links remain open curation items. Neither “missing” nor “not identified” means that no preprint or code was released. Venue/year fields in the original bibliography have not been comprehensively re-audited in this catalogue.', '',
        '## Citation aliases', '',
        '| Work | Citation keys |', '| --- | --- |'
    ]
    for p in papers:
        if len(p['citation_keys']) > 1:
            coverage.append('| ' + cell(p['title']) + ' | ' + ', '.join('`' + k + '`' for k in p['citation_keys']) + ' |')
    coverage += ['', '## arXiv links still to identify', '', rows([p for p in papers if not p['arxiv_url']]), '', '## Code links still to identify', '', rows([p for p in papers if not p['code_url']]), '']
    (ROOT / 'docs' / 'COVERAGE.md').write_text('\n'.join(coverage), encoding='utf-8')
    print(f'Rendered {len(papers)} works in {len(sections)} sections; arXiv={na}, code={nc}.')

if __name__ == '__main__':
    render()
