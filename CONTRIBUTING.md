# Contributing

Suggest work through an issue or pull request. For the [survey homepage](README.md), include the proposed section, title, publication year and venue, and a primary paper or benchmark URL. Add public code, project, or dataset links when available.

## Companion reading list

To contribute to the [companion reading list](docs/READING_LIST.md), also include one sentence explaining the specific visual mechanism and follow the [selection criteria](docs/CURATION.md).

## Add or update a paper

1. Add or correct its entry in `references.bib`. Use the author’s paper, publisher record, official project page, or code repository to establish identity.
2. Add its citation key to `data/selection.json` only after reviewing visual relevance. Record `primary_topic` and a concrete `vision_focus`; an optional `abbreviation` can identify the work in starting-point suggestions. Choose one primary topic from [topic navigation](docs/TOPICS.md).
3. Preserve current citation aliases and earlier dated link evidence. Keep code repositories separate from project pages. Add newly checked primary metadata and links to `data/link-checks.json`, recording `source_url`, `checked_title`, and `checked_at`. Do not invent unverified URLs.
4. Synchronize the catalogue and regenerate the companion reading list. The catalogue uses publication years from 2024 onward, one row per work, and explicit visual contribution summaries.

## Synchronize from the manuscript

```sh
python3 scripts/sync_bibliography.py /path/to/all_references.bib --date YYYY-MM-DD --manuscript-root /path/to/manuscript
python3 scripts/build_readme.py
python3 scripts/validate_catalog.py
```

The source bibliography is copied exactly. New entries remain bibliography-only until explicitly selected. The sync script preserves known links only when paper identities match and refuses selected keys that are absent from the new bibliography. If no manuscript root is available, omit that option; manuscript citation locations are then unavailable for that snapshot.

## Edit inside this repository

After changing `references.bib`, `data/selection.json`, or `data/link-checks.json`, run:

```sh
python3 scripts/sync_bibliography.py references.bib --date YYYY-MM-DD
python3 scripts/build_readme.py
python3 scripts/validate_catalog.py
```

Use the actual snapshot date. The build script updates the companion reading list and its supporting documents. Validation checks admission decisions, identities, dates, primary topics, summaries, counts, local links, and the generated table rows.
