#!/usr/bin/env python3
"""Sync a manuscript bib while keeping reading-list admission explicit.

Usage: python3 scripts/sync_bibliography.py /path/to/all_references.bib --date YYYY-MM-DD
New bibliography entries remain bibliography-only until added to selection.json.
"""
import argparse
import copy
import json
import re
from collections import defaultdict
from pathlib import Path
from bibtex_utils import arxiv_id, bibliography_digest, norm, parse, tex_text, venue
from build_readme import ROOT, read, save


def identity(entry):
    return ('arxiv', arxiv_id(entry)) if arxiv_id(entry) else ('title', norm(tex_text(entry['fields']['title'])))


def sync(source, date, manuscript=None):
    entries, _, errors, recovered = parse(source)
    assert not errors and not recovered, (errors, recovered)
    entries = [e for e in entries if e['type'] != 'ieeetranbstctl']
    bib = {e['key']: e for e in entries}
    assert len(bib) == len(entries), 'Duplicate BibTeX keys'
    selection = read('selection.json')
    assert set(selection) <= set(bib), ('Selected keys absent from new bib; review before syncing', sorted(set(selection) - set(bib)))
    previous = read('papers.json')
    by_arxiv = {p['arxiv_url'].rsplit('/', 1)[-1]: p for p in previous if p.get('arxiv_url')}
    by_title = {norm(t): p for p in previous for t in [p['title']] + p.get('bib_titles', [])}
    groups = defaultdict(list)
    for e in entries:
        groups[identity(e)].append(e['key'])
    checks = read('link-checks.json')
    locations = defaultdict(list)
    input_files = []
    if manuscript:
        paths = [manuscript / 'main.tex']
        paths += [p for folder in ('Secs', 'Tabs', 'Figures') for p in sorted((manuscript / folder).glob('*.tex'))]
        for path in paths:
            if not path.exists():
                continue
            relative = path.relative_to(manuscript).as_posix()
            input_files.append(relative)
            for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                line = re.split(r'(?<!\\)%', line, maxsplit=1)[0]
                for match in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', line):
                    for key in match[1].split(','):
                        key = key.strip()
                        if re.fullmatch(r'[A-Za-z0-9_:.+\-]+', key):
                            locations[key].append({'source': relative, 'line': number})
    papers, decisions, seen = [], {}, set()
    for key, choice in selection.items():
        e = bib[key]
        group = groups[identity(e)]
        assert not set(group) & seen, ('Two selections name the same work', group)
        seen.update(group)
        title = tex_text(e['fields']['title'])
        aid = arxiv_id(e)
        old = by_arxiv.get(aid) if aid else None
        if not old:
            candidate = by_title.get(norm(title))
            # An arXiv mismatch may indicate that an old key was repurposed.
            if candidate and (not aid or not candidate.get('arxiv_url') or candidate['arxiv_url'].endswith('/' + aid)):
                old = candidate
        p = copy.deepcopy(old) if old else {}
        for field in ('legacy_sections', 'legacy_assignments', 'representative_topics', 'classification_basis',
                      'classification_confidence', 'reference_role'):
            p.pop(field, None)
        current_assignments = p.pop('assignments', [])
        previous_assignments = p.get('selection_evidence', {}).get('previous_assignments', current_assignments)
        p.update(id=key, title=title, year=tex_text(e['fields']['year']), venue=venue(e),
                 venue_raw=tex_text(e['fields'].get('booktitle', e['fields'].get('journal', e['fields'].get('xxxjournal', '')))),
                 citation_keys=group, bib_titles=[tex_text(bib[k]['fields']['title']) for k in group],
                 bib_years=[tex_text(bib[k]['fields']['year']) for k in group],
                 primary_topic=choice['primary_topic'], sections=[choice['primary_topic']],
                 vision_focus=choice['vision_focus'], curated_at=date)
        p['legacy_citation_keys'] = sorted(set(p.get('legacy_citation_keys', []) + (old.get('citation_keys', []) if old else [])) - set(group))
        p['arxiv_url'] = 'https://arxiv.org/abs/' + aid if aid else p.get('arxiv_url')
        p['arxiv_status'] = p.get('arxiv_status') or ('bibliography_supplied' if aid else 'not_identified')
        supplied = tex_text(e['fields'].get('url', e['fields'].get('xxxurl', '')))
        if supplied and re.match(r'https?://', supplied):
            if 'github.com' in supplied:
                if not p.get('code_url'):
                    p['code_url'] = supplied
                    p['code_status'] = 'bibliography_supplied'
            else:
                p['paper_url'] = supplied
        for field in ('paper_url', 'code_url', 'project_url'):
            p.setdefault(field, None)
        for field in ('additional_code_urls', 'additional_project_urls', 'link_evidence', 'source_urls'):
            p.setdefault(field, [])
        p.setdefault('code_status', 'not_identified')
        if key in checks:
            check = checks[key]
            assert norm(check['checked_title']) == norm(title), ('Checked title does not match bibliography', key)
            checked_evidence = dict(check, citation_key=key)
            if checked_evidence not in p['link_evidence']:
                p['link_evidence'].append(checked_evidence)
            p['source_urls'] = list(dict.fromkeys(p['source_urls'] + [check['source_url']]))
            if 'arxiv.org/abs/' in check['source_url']:
                p['arxiv_url'] = check['source_url']
                p['arxiv_status'] = 'verified_title'
            if check.get('arxiv_url'):
                p['arxiv_url'] = check['arxiv_url']
                p['arxiv_status'] = 'verified_title'
            for field in ('code_url', 'project_url'):
                if check.get(field):
                    p[field] = check[field]
                    if field == 'code_url':
                        p['code_status'] = 'verified_primary_link'
        if p.get('code_status') == 'bibliography_supplied':
            supplied_evidence = {'kind': 'bibliography_supplied', 'citation_key': key, 'source_url': supplied, 'imported_at': date}
            if supplied_evidence not in p['link_evidence']:
                p['link_evidence'].append(supplied_evidence)
        evidence = [loc for k in group for loc in locations.get(k, [])]
        basis = 'current_manuscript_discussion' if evidence else ('retained_catalogue_evidence' if old else 'bibliography_editorial_selection')
        p['selection_evidence'] = {'basis': basis, 'manuscript_locations': evidence,
                                   'previous_assignments': previous_assignments,
                                   'primary_source_checks': [checks[key]] if key in checks else [],
                                   'note': 'Visual summary and primary-topic placement are editorial curation; no complete new full-paper audit is claimed.'}
        p['assignments'] = [{'section': choice['primary_topic'], 'source': 'data/selection.json',
                             'classification': 'explicit_vision_curation', 'citation_key': key}]
        p['bibliography_evidence'] = {'source': 'references.bib', 'citation_keys': group, 'imported_at': date}
        previous_name = p.get('abbreviation')
        if previous_name == '—':
            previous_name = None
        p['abbreviation'] = choice.get('abbreviation') or previous_name or (title.split(':', 1)[0] if ':' in title else None)
        papers.append(p)
        for k in group:
            decisions[k] = {'status': 'selected', 'work_id': key, 'primary_topic': choice['primary_topic'], 'reason': choice['vision_focus']}
    for key, e in bib.items():
        if key in decisions:
            continue
        title, year = tex_text(e['fields']['title']), int(tex_text(e['fields']['year']))
        if year < 2024:
            reason = 'historical_reference_outside_recent_reading_list'
        elif key in {'yao2022react', 'zhang2026hyperagents', 'shrivastava2026echo', 'lu2026paw', 'zuo2026qwenagentworld', 'yu2026openforgerl', 'li2026agent', 'zhou2024webarena', 'chae2025wma', 'gu2025webdreamer', 'lee2026rda'}:
            reason = 'general_or_text_agent_background_without_a_selected_visual_mechanism'
        elif key.startswith(('ds_', 'b43_', 'sec6_')) or key in {'bai2025qwen3', 'hu2024ella', 'black2024pi_0'}:
            reason = 'supporting_dataset_model_or_benchmark_not_selected_for_visual_agent_focus'
        else:
            reason = 'not_selected_in_this_editorial_reading_list'
        decisions[key] = {'status': 'bibliography_only', 'year': year, 'title': title, 'reason': reason}
    (ROOT / 'references.bib').write_bytes(source.read_bytes())
    save('papers.json', sorted(papers, key=lambda p: p['id']))
    save('curation.json', {'snapshot_date': date, 'minimum_publication_year': 2024, 'decisions': decisions})
    save('source-map.json', {'main_source': 'main.tex', 'source_snapshot': date, 'input_files': input_files,
                            'method': 'Current citation locations; explicit selection is independent from manuscript citation coverage.',
                            'citation_locations': {k: v for k, v in locations.items() if k in bib},
                            'unresolved_manuscript_citations': {k: v for k, v in locations.items() if k not in bib},
                            'effective_sections_by_citation_key': {k: p['sections'] for p in papers for k in p['citation_keys']},
                            'assignment_evidence': {p['id']: p['assignments'] for p in papers}})
    taxonomy = read('taxonomy.json')
    taxonomy.update(source='survey framework hierarchy; independently curated reading-list selections', snapshot_date=date)
    for branch in taxonomy['branches']:
        for category in branch['categories']:
            for topic in category['topics']:
                topic.pop('works', None)
                topic['selected_citation_keys'] = [p['id'] for p in papers if p['primary_topic'] == topic['id']]
    taxonomy['validation'] = {'branches': 2, 'categories': 10, 'topics': 35, 'planning_branch': 'external',
                              'catalogue_bibliography_sha256': bibliography_digest(source)}
    save('taxonomy.json', taxonomy)
    meta = read('metadata.json')
    meta = {k: v for k, v in meta.items() if k in {'assembled_at'}}
    meta.update(snapshot_date=date, minimum_publication_year=2024, selection_policy='explicit_vision_curation')
    save('metadata.json', meta)
    print(f'Synced {len(bib)} bibliography keys; selected {len(papers)} unique works; {len(decisions) - len(seen)} bibliography-only keys.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bibliography', type=Path)
    parser.add_argument('--date', required=True)
    parser.add_argument('--manuscript-root', type=Path)
    args = parser.parse_args()
    sync(args.bibliography, args.date, args.manuscript_root)
