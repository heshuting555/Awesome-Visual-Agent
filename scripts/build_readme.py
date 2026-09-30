#!/usr/bin/env python3
"""Render the year/venue catalogue and secondary survey topic archive."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from bibtex_utils import parse

ROOT = Path(__file__).resolve().parents[1]
PREPRINTS = {'arXiv', 'OpenReview Preprint', 'Preprints.org', 'Venue Unspecified'}
NONPAPERS = {'Official Release', 'Blog'}


def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;').replace('[', '&#91;').replace(']', '&#93;')


def anchor(section):
    return 'section-' + section.replace('.', '-')


def venue_anchor(year, venue):
    return 'year-' + str(year) + '-' + re.sub(r'[^a-z0-9]+', '-', venue.lower()).strip('-')


def venue_order(venue):
    return (2 if venue in NONPAPERS else 1 if venue in PREPRINTS else 0, venue.casefold())


def rows(papers):
    out = ['| Year | Venue | Paper Abbr | Paper Title | Project/Code |', '| :---: | :---: | :---: | --- | :---: |']
    for p in sorted(papers, key=lambda p: (-int(p['year']), p['title'].casefold(), p['id'])):
        url = p.get('paper_url') or p.get('arxiv_url') or p.get('project_url') or p.get('code_url')
        title = '[' + cell(p['title']) + '](' + url + ')' if url else cell(p['title'])
        if p.get('arxiv_url') and p['arxiv_url'] != url:
            title += ' · [arXiv](' + p['arxiv_url'] + ')'
        projects = list(dict.fromkeys(([p['project_url']] if p.get('project_url') else []) + p.get('additional_project_urls', [])))
        codes = list(dict.fromkeys(([p['code_url']] if p.get('code_url') else []) + p.get('additional_code_urls', [])))
        resources = []
        for label, urls in [('Project', projects), ('Code', codes)]:
            resources += ['[' + (label if len(urls) == 1 else label + ' ' + str(i + 1)) + '](' + u + ')' for i, u in enumerate(urls)]
        resource_cell = ' · '.join(resources) or ('Unavailable' if p.get('code_status') == 'official_link_unavailable' else '—')
        out.append('| ' + ' | '.join([cell(p['year']), cell(p['venue']), cell(p.get('abbreviation', '—')), title, resource_cell]) + ' |')
    return '\n'.join(out)


def render():
    papers, sections, meta = read('papers.json'), read('sections.json'), read('metadata.json')
    entries, _, errors, _ = parse(ROOT / 'references.bib')
    assert not errors, errors
    keys = {e['key'] for e in entries if e['type'] != 'ieeetranbstctl'}
    na = sum(bool(p['arxiv_url']) for p in papers)
    nc = sum(bool(p['code_url']) for p in papers)
    years = sorted({p['year'] for p in papers}, key=int, reverse=True)
    counts = Counter(p['year'] for p in papers)
    venues = {year: sorted({p['venue'] for p in papers if p['year'] == year}, key=venue_order) for year in years}
    meta.update(unique_works=len(papers), arxiv_links=na, code_links=nc, bibliography_keys=len(keys), bibliography_sha256=hashlib.sha256((ROOT / 'references.bib').read_bytes()).hexdigest(), organization='year_then_venue', year_counts={year: counts[year] for year in years})
    (ROOT / 'data/metadata.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    main = [
        '# 🔍 Seeing the Horizon of Vision Agent: A Survey', '',
        '**Awesome Vision Agents** — papers, benchmarks, projects, and code.', '',
        f'**{len(papers)} unique works** · **{na} arXiv links** · **{nc} works with code links** · **{len(keys)} BibTeX keys**', '',
        '💡 Welcome! This collection accompanies our survey on vision agents. It covers visual perception and reasoning, agent harnesses, memory, capability evolution, GUI and embodied applications, and evaluation.', '',
        '📌 Corrections and additions are welcome through [issues](https://github.com/heshuting555/Awesome-Vision-Agent/issues) or pull requests. See the [contribution guide](CONTRIBUTING.md).', '',
        '[📖 Full bibliography](references.bib) · [📦 Machine-readable catalogue](data/papers.json) · [🔎 Coverage and provenance](docs/COVERAGE.md) · [🗂 Survey topic archive](docs/TOPICS.md)', '',
        '## Introduction', '',
        'Papers are currently organized by **year, newest first**, then by **conference or publication venue**. Each work appears once in the main list. The table format follows [Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications).', '',
        '**Reading the tables.** Years and venues follow the bibliography; venue names are standardized. Workshops, Findings, and Demos are labeled separately. Preprints have their own groups, and journals and official releases retain distinct labels. A published version takes precedence over its preprint when both refer to the same work; all BibTeX keys are retained. A dash (—) means a name or link has not been identified, rather than that no implementation exists. Paper abbreviations use names present in the title. Code/project links retain primary-source evidence and check dates. Newly added author-supplied code URLs are distinguished from previously checked repositories in the catalogue.', '',
        f'Bibliography snapshot: **{meta["snapshot_date"]}**. Venue/year fields have not all been independently re-audited; supporting evidence is tracked in [coverage notes](docs/COVERAGE.md).', '',
        '## 📚 Table of Contents', ''
    ]
    for year in years:
        main += ['- [' + year + '](#year-' + year + ') — ' + str(counts[year]) + (' work' if counts[year] == 1 else ' works'), '  - ' + ' · '.join('[' + venue + '](#' + venue_anchor(year, venue) + ')' for venue in venues[year])]
    main += ['', '## 📑 Paper List', '']
    for year in years:
        main += ['<a id="year-' + year + '"></a>', '', '## 📅 ' + year, '']
        for venue in venues[year]:
            items = [p for p in papers if p['year'] == year and p['venue'] == venue]
            main += ['<a id="' + venue_anchor(year, venue) + '"></a>', '', '### ' + venue, '', rows(items), '']
    main += ['## 🙏 Acknowledgements', '', 'The table presentation is inspired by [Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications). The earlier topic archive also drew on [Awesome-Agentic-MLLMs](https://github.com/HJYao00/Awesome-Agentic-MLLMs). Linked papers and software retain their respective authorship and licenses.', '', '## 📝 Citation', '', 'Use [references.bib](references.bib) to cite the individual works. A citation for the survey will be added when its public bibliographic record is available.', '']
    (ROOT / 'README.md').write_text('\n'.join(main), encoding='utf-8')
    # Keep prior topic links and evidence available as a secondary view.
    by_section = {s['id']: [p for p in papers if s['id'] in p['sections']] for s in sections}
    topic_index = ['# Survey topic archive', '', '[← Year and venue catalogue](../README.md)', '', 'Existing topic assignments retain their evidence. Newly imported works with a topic assignment still to review are listed in the additional-reference appendix.', '']
    for chapter in [s for s in sections if s['depth'] == 1]:
        sid = chapter['id']
        topic_index.append('- [' + sid + '. ' + chapter['title'] + '](chapters/' + sid + '.md)')
        lines = ['# ' + sid + '. ' + chapter['title'], '', '[← Main catalogue](../../README.md) · [Topic archive](../TOPICS.md)', '']
        for s in [s for s in sections if s['id'] == sid or s['id'].startswith(sid + '.')]:
            lines += ['<a id="' + anchor(s['id']) + '"></a>', '', '#' * min(s['depth'] + 1, 4) + ' ' + s['id'] + '. ' + s['title'], '']
            if by_section[s['id']]:
                lines += [rows(by_section[s['id']]), '']
            elif not any(by_section[t['id']] for t in sections if t['id'].startswith(s['id'] + '.')):
                lines += ['References for this framing section are listed under their relevant topics.', '']
        (ROOT / 'docs/chapters' / (sid + '.md')).write_text('\n'.join(lines), encoding='utf-8')
    (ROOT / 'docs/TOPICS.md').write_text('\n'.join(topic_index) + '\n', encoding='utf-8')
    audit = read('bibliography-update.json')
    coverage = [
        '# Catalogue coverage and provenance', '',
        f'Bibliography snapshot and catalogue update: **{meta["snapshot_date"]}**. Original catalogue assembled: **{meta["assembled_at"]}**. Historical evidence retains its original dates.', '',
        '| Item | Count |', '| --- | ---: |',
        f'| Bibliographic keys | {len(keys)} |',
        f'| Non-paper BibTeX control records (excluded) | {meta["nonpaper_records"]} |',
        f'| Unique works after merging aliases | {len(papers)} |',
        f'| Existing works preserved | {audit["preserved_existing_works"]} |',
        f'| Newly imported works | {audit["imported_works"]} |',
        f'| Works with an arXiv link | {na} |',
        f'| Works with code links | {nc} |',
        f'| Works without an identified paper or arXiv link | {sum(not p["arxiv_url"] and not p["paper_url"] for p in papers)} |',
        f'| Works without an identified code link | {len(papers)-nc} |', '',
        '## Organization and bibliography', '',
        'The main README groups each unique work by bibliography year and normalized venue. Workshops, Findings, Demos, preprints, journals, and official releases are labeled separately. For a verified preprint/published pair, the published record supplies the displayed year, venue, and title. All current BibTeX keys are preserved in references.bib, including the string definitions and bibliography control record.', '',
        'The [topic archive](TOPICS.md) preserves previous survey-section assignments. New works whose topic has not been reviewed are assigned to the additional-reference appendix. Active-citation positions in [source-map.json](../data/source-map.json) were refreshed from the current manuscript input graph. Filenames and citation positions are retained without publishing manuscript prose.', '',
        '## Identity corrections and aliases', '',
        'The historical catalogue used `chen2026reflect` for Reflect-R1 (arXiv:2606.27922). The current bibliography uses that key for Reflect, Revise, Reuse (arXiv:2609.17653). Reflect-R1 is now recorded under `chen2026reflectr1`; these remain separate works with their own links and evidence.', '',
        'MMBench-GUI and MobileUse each have a preprint title and a published title for the same arXiv identity. Each pair appears once in the README, while both current BibTeX keys are preserved. Historical aliases and original assignment keys remain in the catalogue evidence. The [bibliography update record](../data/bibliography-update.json) lists migrations, imports, and identity repairs.', '',
        '| Work | Current citation keys |', '| --- | --- |'
    ]
    for p in papers:
        if len(p['citation_keys']) > 1:
            coverage.append('| ' + cell(p['title']) + ' | ' + ', '.join('`' + k + '`' for k in p['citation_keys']) + ' |')
    coverage += ['', '## Verification scope', '',
        'The merged bibliography passed syntax, duplicate-key, manuscript-reference, and BibTeX compilation checks in the source workspace. Selected title, author, and publication details were corrected using official arXiv and conference/publisher metadata before import. These checks do not establish that every venue/year label in the full library has been independently re-audited.', '',
        'arXiv links preserve previously verified identities or official citation-title checks. New code links may come directly from an author abstract; these use `verified_author_supplied_link` and do not claim a fresh repository availability check. Existing repository checks retain their original dates. Project/model pages remain separate from code. Missing links are curation items; working links do not establish experimental reproducibility.', '',
        '## Paper links still to identify', '', rows([p for p in papers if not p['arxiv_url'] and not p['paper_url']]), '',
        '<details>', '<summary>Code links still to identify</summary>', '', rows([p for p in papers if not p['code_url']]), '', '</details>', '']
    (ROOT / 'docs/COVERAGE.md').write_text('\n'.join(coverage), encoding='utf-8')
    print(f'Rendered {len(papers)} works in {len(years)} years; arXiv={na}, code={nc}.')


if __name__ == '__main__':
    render()
