# Contributing

Corrections and additions are welcome. Include the paper title, publication year and venue, arXiv or publisher URL, and the author's code/project link. The main README is currently organized by year, then conference or publication venue. Survey-topic assignments remain available in the secondary topic archive.

## Update an existing entry

1. Locate its title or BibTeX key in `data/papers.json`.
2. Verify the link using the paper, an author project page, or a repository README that identifies the paper. Record the supporting URL and evidence. Keep project pages separate from code repositories.
3. Preserve current citation-key aliases and the existing section-assignment evidence. Keep removed historical keys in `legacy_citation_keys` and original assignment keys in `original_citation_key`. Record a new topical placement only with its supporting basis.
4. Update verification dates and source evidence when rechecking a link.
5. Regenerate and validate the Markdown:

```sh
python3 scripts/build_readme.py
python3 scripts/validate_catalog.py
```

Both scripts use the Python standard library (Python 3.9+). Edit the JSON source; generated README, coverage notes, and topic archive pages will be overwritten by the renderer. Each unique work must appear exactly once in the main README.

## Add a new work

Add its BibTeX record to `references.bib`, then a corresponding catalogue record to `data/papers.json`. Check for an existing title or arXiv identity first and add an alias instead of duplicating a work. Set `year`, `venue`, `venue_raw`, and `abbreviation` from the primary record; `scripts/bibtex_utils.py` standardizes venue names. Use the published record as the canonical `id` when merging a preprint with its published version. Keep Workshops, Findings, and Demos separate from the main conference. Use `—` for an abbreviation that is not explicit in the title.

Preserve verification evidence and distinguish an author-supplied code URL (`verified_author_supplied_link`) from a repository whose availability and identity have been checked. Use `null` with `not_identified` for unresolved links. Retain topic IDs from `data/sections.json`; use the additional-reference appendix (`A`) while a new work's topic is pending review. The renderer refreshes counts and the bibliography SHA-256 in `data/metadata.json` automatically. Citation counts and source-map evidence must be kept consistent with the imported bibliography.

Do not infer a repository URL from a model or paper name. Missing links are open curation items, not claims that code is unavailable.
