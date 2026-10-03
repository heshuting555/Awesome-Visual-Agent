# Contributing

Corrections and additions are welcome. Include the paper title, publication year and venue, arXiv or publisher URL, and the author's code/project link. The main catalogue follows the current Figure 1 framework: internal capabilities and harness infrastructure, with planning and orchestration in the harness branch. Use [framework navigation and topic IDs](docs/TOPICS.md) or `data/taxonomy.json` to choose a topic.

## Update an existing entry

1. Locate its title or BibTeX key in `data/papers.json`.
2. Verify links using the paper, an author project page, or a repository README that identifies the paper. Record the supporting URL and evidence. Keep project pages separate from code repositories.
3. Preserve citation-key aliases and verification evidence. Keep removed historical keys in `legacy_citation_keys`, original assignment keys in `original_citation_key`, and earlier draft placements in `legacy_sections` and `legacy_assignments`.
4. For a topic change, select valid topic IDs from `data/taxonomy.json`. Record each placement in `assignments` with `section`, `source`, `classification`, and `citation_key`; explain the mechanism or source that supports it. Distinguish a current manuscript citation, a legacy-topic mapping, and a title-based curation inference.
5. Update verification dates and source evidence when rechecking a link, then regenerate and validate:

```sh
python3 scripts/build_readme.py
python3 scripts/validate_catalog.py
```

Both scripts use the Python standard library. Edit JSON sources; the README, framework navigation, and coverage notes are generated. Existing `docs/chapters/` pages preserve the old manuscript archive and are labeled as historical.

## Assign topics

- `sections` is a nonempty list of current Figure 1 topic IDs, with no duplicates. A work may support multiple topics and appear in several main tables; it must appear **at most once within each topic**.
- `primary_topic` is one of those IDs and identifies the work's main placement.
- `representative_topics` lists topics where the work was explicitly selected in Figure 1; it is empty for other works. Change representative selections through the taxonomy and figure source together, rather than adding a star independently.
- `assignments` records the sources behind current placements. Several source records may support one work/topic pair without producing duplicate table rows.

The renderer puts Figure 1 representatives first, marked ★ in the figure's order, then orders other works alphabetically by title. Years and venues are descriptive table fields. Counts distinguish unique works from topic placements, so cross-listing does not inflate the bibliography size.

## Add a new work

Add its BibTeX record to `references.bib`, then a corresponding record to `data/papers.json`. Check for an existing title, DOI, or arXiv identity first; add an alias when the work already exists. Set `year`, `venue`, `venue_raw`, and `abbreviation` from the primary record. Use `—` for an abbreviation that is not identified. Keep publication details and title variants as metadata, and preserve all current citation keys when merging a preprint with its published version.

Choose at least one valid current topic and document its basis. Use an empty `representative_topics` list unless Figure 1 explicitly selects the work. If the mechanism is unclear, open an issue with the source and proposed placement rather than inventing a topic or silently using an old appendix ID.

Preserve verification evidence and distinguish an author-supplied code URL (`verified_author_supplied_link`) from a repository whose availability and paper identity have been checked. Use `null` with `not_identified` for unresolved links. The renderer refreshes coverage counts and the bibliography SHA-256 in `data/metadata.json`.

Do not infer a repository URL from a model or paper name. Missing links are open curation items, not claims that code is unavailable.
