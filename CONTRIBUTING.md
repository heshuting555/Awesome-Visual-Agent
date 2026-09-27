# Contributing

Corrections and additions are welcome. Include the paper title, arXiv or publisher URL, the author's code/project link, and the survey section where the work belongs.

## Update an existing entry

1. Locate its title or BibTeX key in `data/papers.json`.
2. Verify the link using the paper, an author project page, or a repository README that identifies the paper. Record the supporting URL and evidence. Keep project pages separate from code repositories.
3. Preserve citation-key aliases and the existing section-assignment evidence. Record a new placement as a topical assignment unless it is supported by an actual manuscript citation.
4. Update verification dates and source evidence when rechecking a link.
5. Regenerate and validate the Markdown:

```sh
python3 scripts/build_readme.py
python3 scripts/validate_catalog.py
```

Both scripts use the Python standard library. Edit the JSON source; generated README and chapter pages will be overwritten by the renderer.

## Add a new work

Add its BibTeX record to `references.bib`, then a corresponding catalogue record to `data/papers.json`. Check for an existing title or arXiv identity first and add an alias instead of duplicating a work. Assign one or more IDs from `data/sections.json`, preserve verification evidence, and use `null` with `not_identified` for unresolved links. The renderer refreshes the bibliography count, unique-work count, coverage counts and SHA-256 in `data/metadata.json` automatically.

Do not infer a repository URL from a model or paper name. Missing links are open curation items, not claims that code is unavailable.
