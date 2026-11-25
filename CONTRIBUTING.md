# Contributing

Suggest work through an issue or pull request. For the [survey homepage](README.md), include the proposed section, title, publication year and venue, and a primary paper or benchmark URL. Add public code, project, or dataset links when available.

## Add or update a paper

1. Add or correct its entry in `references.bib`. Use the author’s paper, publisher record, official project page, or code repository to establish identity.
2. Add its citation key to `data/selection.json` only after reviewing visual relevance. Choose one `primary_topic` from [the catalogue taxonomy](data/taxonomy.json) and record a concrete `vision_focus`.
3. Preserve current citation aliases and earlier dated link evidence. Keep code repositories separate from project pages. Add newly checked primary metadata and links to `data/link-checks.json`, recording `source_url`, `checked_title`, and `checked_at`. Do not invent unverified URLs.
4. Synchronize the catalogue and rebuild its metadata. The catalogue uses publication years from 2024 onward and records one entry and a visual contribution summary per selected work.

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

Use the actual snapshot date. The build script refreshes `data/metadata.json`. Validation checks catalogue entries against the bibliography and selection data, along with local links and the entry counts shown in the homepage tables.
