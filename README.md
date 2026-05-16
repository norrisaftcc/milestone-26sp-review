# milestone-26sp-review
26SP Review of Objectives and Work

This repository and binder have been implemented using the Algocratic Futures "Sacred Workflow" method.
They serve to demonstrate iterative software development using a team of AI agents.
See Issues and Pull Requests for supplemental documentation.

## Building the binder for review

The binder is assembled by converting the markdown sources in `inputs/` to `.docx` files in `outputs/` via pandoc. The designer reviews the `.docx` files for style and InDesign-import readiness (per the audit in [PR #9](https://github.com/norrisaftcc/milestone-26sp-review/pull/9)); the author reviews for tone and content.

### Prerequisites

`pandoc` on PATH. Install once:

```bash
brew install pandoc        # macOS
sudo apt install pandoc    # Ubuntu/Debian
```

### Run the build

From the repo root:

```bash
scripts/build_binder.sh
```

Use `--clean` to wipe `outputs/*.docx` before rebuilding:

```bash
scripts/build_binder.sh --clean
```

### What gets built

Eight `.docx` files land flat in `outputs/`, in binder read order — six binder chapters plus the two-file supporting research appendix:

| Output | Source | Role |
|---|---|---|
| `01_Introduction.docx` | `inputs/01_Introduction.md` | Binder front matter — what this binder documents, the dy/dx methodological thread, the in-character apparatus |
| `02_Executive_Summary.docx` | `inputs/02_Executive_Summary.md` | One-page synthesis: metrics, per-objective summaries, bottom line |
| `03_Objective_1_Cross-Departmental_Capstone_Collaboration_Framework.docx` | `inputs/03_*.md` | Obj 1 detail (cross-departmental capstone) |
| `04_Objective_2_Source_Control_Version_Control_Instructional_Modules.docx` | `inputs/04_*.md` | Obj 2 detail (SCVC instructional modules) |
| `05_Objective_3_Ghost_Student_Discovery_Tool.docx` | `inputs/05_*.md` | Obj 3 detail (Ghost Tool / PM support) |
| `06_Performance_Objective_Zero.docx` | `inputs/06_*.md` | Foundational meta-objective (AlgoCratic Futures architecture, Dilts six-level model) |
| `07_capstone_research_support.docx` | `inputs/supporting_documentation/07_*.md` | Appendix — Obj 1 supporting research |
| `08_ghost_tool_research_support.docx` | `inputs/supporting_documentation/08_*.md` | Appendix — Obj 3 supporting research (ghost-student fraud brief) |

Not built into the binder:

- `inputs/supporting_documentation/Adjacent_Faculty_Engagement.md` — appendix reference material kept alongside the binder but not part of the built `.docx` set.
- `inputs/# Purpose of work.md` and `inputs/raw_material/# PHILOSOPHICAL ISSUES.md` — author scratchpads, not binder content.

### Reference doc (style consistency)

If a Word reference document exists at `inputs/design/binder-reference.docx`, the build picks it up automatically via pandoc's `--reference-doc=` flag, producing `.docx` output that conforms to the unified style set defined in [`inputs/design/Binder_Style_and_InDesign_Audit.md`](inputs/design/Binder_Style_and_InDesign_Audit.md).

If the reference doc is absent, the build falls back to pandoc's defaults so the designer has concrete output to react to on the first pass. Creating the reference doc is a follow-up once the designer settles on fonts (item 1 in the audit's "needing human judgment" list).
