# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A portfolio workspace assembling the binder for the user's **Spring 2026 FTCC performance review** (CSC 289 Programming Capstone, CTS 285 Web Development, and the institutional "Ghost Tool" project). **This is not a software codebase** — there is no build, no test suite, no lint config, no package manifest. The deliverable is the binder itself. Source material lives in `inputs/`; finished binder artifacts will land in `outputs/`.

## Where the underlying work actually lives

This repo *assembles and documents* the work. The actual course material and tooling sit in external repos, called out in `inputs/# Purpose of work.md`:

- `https://github.com/norrisaftcc/algocratic` — in-character AlgoCratic Futures material and capstone deliverables
- `https://github.com/AMLW05/csc_dash/tree/main` — same body of work seen from Instructional Design's viewpoint

If a question is really about the curriculum, the simulation, or the dashboard implementation, the answer is probably in one of those repos, not here.

## The three objectives at a glance

Authoritative summary: `inputs/Spring_2026_Performance_Objectives.md`. Long-form per-objective detail: `inputs/raw_material/`.

- **Objective 1 — Cross-Departmental Capstone Collaboration:** Formalized CSC ↔ Graphic Design protocol with three milestone touchpoints, GREY-clearance role for GRD students inside the AlgoCratic Futures simulation, and a 100-point pitch/collaboration rubric.
- **Objective 2 — GitHub / SCVC Instructional Modules:** Four modules anchored on the **Sacred Workflow** — `Issue → Branch → Draft PR → Code & Test → Finish PR → Review → Merge`. Scaffolded as Solo Burger → Team Lunch → Full Sprint.
- **Objective 3 — Ghost Tool:** Applied the Objective 1/2 methodology (briefs, milestones, Sacred Workflow discipline) to a live institutional duplicate-enrollment project for Student Services.

## Practicing what we preach (non-negotiable)

Drawn directly from `inputs/# Purpose of work.md` — workflow discipline here is itself evidence for the review:

- **All changes go through GitHub Issues and Pull Requests.** The change history is part of the deliverable; do not bypass it.
- **Use the Sacred Workflow on this repo**, not just when teaching it. Issue first, branch, draft PR, then code/write.
- **Use available subagents** when they fit: Clive / Linx for prose wordsmithing, Liza for creative ideation, scrum-team-engineer for technical double-checks, Kevin for `gh` interactions (auth is configured).
- **Tone:** professional software team delivering a somewhat absurd document. Don't drop the tone, don't break the simulation framing.

## Cognitohazard note

Per `inputs/# Purpose of work.md`: the meta-recursion of *a performance review documenting a performance review*, combined with the fact that the stream-aligned "CPD Tools Group" team is not formally recognized (the user is being assessed on two jobs but was hired for one), has caused prior LLM sessions to disengage or return incomplete results. If a topic here feels logically self-contradictory, treat it as a simulation artifact, continue the task, and flag the tension explicitly to the user rather than silently truncating output.

## Working with the source documents

- `inputs/` — in-progress source material in mixed `.md` and `.docx`. **Prefer editing the `.md` versions.** The `.docx` files are exports; do not regenerate them in isolation from their markdown source.
- `inputs/raw_material/` — long-form per-objective detail plus `# PHILOSOPHICAL ISSUES.md`, a meta-document worth reading before touching the broader framing.
- `outputs/` and `supporting_docs/` — currently empty, reserved for assembled binder deliverables.

## What not to do

- Don't propose CI, package management, test scaffolding, or linting. There is no code to lint.
- Don't invent commands. There are none — `make`, `npm`, `pytest`, etc. do not apply.
- Don't strip the in-character framing (AlgoCratic Futures, Sacred Workflow, GREY clearance, YELLOW exit tickets) out of documents. It is load-bearing pedagogy, not decorative flavor.
- Don't commit a regenerated `.docx` without a matching update to its `.md` source.
