# Reading-list selection

[← Selected catalogue](../README.md)

The GitHub reading list highlights recent vision-centric agent research. The manuscript bibliography also includes background and supporting references; a citation in the paper does not automatically qualify a work for this list.

## Inclusion criteria

1. **Recent publication:** the current list uses publication years 2024–2026, as recorded in the survey bibliography. An earlier preprint of a selected conference paper is acceptable.
2. **A concrete visual contribution:** observations, pixels, image regions, video intervals, 3D geometry, screen states, or rendered results must materially affect reasoning or interaction. Visual input alone is insufficient.
3. **Agent relevance:** prioritize active perception, tool-mediated visual reasoning, grounded action, action-conditioned world models, visual memory, observed-result verification, and improvement from visual feedback. Benchmarks must directly evaluate visual-agent mechanisms or behavior.
4. **A clear reason to read it:** each selected paper has an individual `vision_focus` summary. Selection considers mechanism diversity and coverage across GUI, video, robotics, driving, scientific imaging, and visual generation. It does not attempt to include every eligible paper.
5. **Traceable identity:** retain a paper or publisher link, match its current citation key, and preserve dated evidence for project and code URLs. Missing code is allowed.

## What stays in the bibliography

Historical foundations such as active-vision theory, ReAct, MM-REACT, ViperGPT, CLIP-era models, and early datasets can support the manuscript’s introduction and background. They do not appear in the current recent-work tables.

Recent general or text-agent work also requires a visual reason for inclusion. Hyperagents, terminal-agent ECHO, language-only world models, general harness surveys, and similar references are retained for context. A recent date, an “agent” name, or a place in the manuscript figure does not by itself establish a visual contribution.

General-purpose VLM reports, broad visual QA/video datasets, and standalone generation primitives are supporting resources. We instead highlight work that turns visual capabilities into inspection decisions, grounded interaction, memory, simulation, or verification. For example, ScreenSpot-Pro and VisualWebArena directly test visual GUI grounding and visual web tasks; a broad static video-QA dataset is not automatically selected.

Visual predictive models are included when they directly support control, planning, or interactive environment simulation. Robotics safety work is included for its connection to grounded action constraints, execution monitoring, or evaluation of embodied agents, rather than generic safety discussion.

## Organization and display

The survey’s two branches, ten categories, and thirty-five topics provide navigation. Each paper appears once under its primary contribution, with newest publication years first. The **Vision contribution** column supplies the selection rationale.

The previous Figure 1 star labels have been removed. Suggested starting points illustrate mechanisms and are editorial choices; they are not importance rankings. The GitHub selections are independent of the manuscript figure’s representative examples.

## Decisions and maintenance

[data/selection.json](../data/selection.json) is the explicit admission list. [data/curation.json](../data/curation.json) records a decision for every current bibliography key, including bibliography-only references. “Not selected” describes this reading list’s scope, not paper quality or lack of relevance to the survey.

Updating the bibliography does not automatically add papers to the catalogue. Review new entries against these criteria, add their visual summaries and primary topics to the admission list, and regenerate. If a selected key disappears from the source bibliography, the sync script stops so the maintainer can review the identity or selection change.

Previous generated chapter catalogues have been retired; Git history preserves their earlier contents. Current citation locations and primary-link evidence remain in the machine-readable data.
