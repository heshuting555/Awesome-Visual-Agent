# Catalogue sources and verification

Bibliography snapshot: **2026-10-05**.

| Item | Count |
| --- | ---: |
| Survey bibliography keys | 380 |
| Selected unique works | 195 |
| Selected citation keys | 195 |
| Bibliography-only keys | 185 |
| Papers with arXiv links | 191 |
| Papers with code links | 110 |

## Sources

- [references.bib](../references.bib) is an exact copy of the current manuscript’s `all_references.bib`.
- [selection.json](../data/selection.json) records explicit inclusion, primary topics, and visual contributions.
- [curation.json](../data/curation.json) accounts for every current bibliography key as selected or bibliography-only.
- [papers.json](../data/papers.json) preserves primary links and their dated verification evidence.
- [source-map.json](../data/source-map.json) records current manuscript citation locations and selection evidence.
- [metadata.json](../data/metadata.json) records counts and the bibliography SHA-256.

## Verification scope

Newly checked official arXiv and publisher pages are dated in each record’s `link_evidence`. Earlier link checks retain their original dates. URLs copied from the bibliography use `bibliography_supplied`; they do not claim a fresh availability check. Code/project links are carried over only when the paper identity matches. Missing links remain blank.

Visual contribution summaries are editorial descriptions supported by manuscript discussion, retained source evidence, and newly checked abstracts. Their source types remain distinct in the catalogue. Selection does not claim a complete new full-paper audit or a ranking.

## Rebuild

```sh
python3 scripts/build_readme.py
python3 scripts/validate_catalog.py
```

The validator checks bibliography identities, explicit inclusion, date bounds, coverage decisions, one-topic placement, visual summaries, metadata, and all local Markdown links and anchors. A bibliography update cannot automatically promote papers into the reading list.

## Manuscript citation gaps

The current source scan found **17 citation keys** absent from the supplied bibliography. They remain recorded in [source-map.json](../data/source-map.json) and are not silently imported into the reading list.

`alonso2024diamond`, `b43_referit3d`, `b43_scanrefer`, `bansal2026videophy`, `feng2026newton`, `ghosh2023geneval`, `jain2026weaver`, `kamath2025geneval`, `li2025drivevlaw0`, `meng2024towards`, `niu2025wise`, `wang2026vlaworld`, `wu2026uioceanus`, `xiao2025worldenv`, `xu2026muse`, `zhu2025astra`, `zhu2026clarify`
