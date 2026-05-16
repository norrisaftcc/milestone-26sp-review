# milestone-26sp-review
26SP Review of Objectives and Work

This repository and binder have been implemented using the Algocratic Futures "Sacred Workflow" method.
They serve to demonstrate iterative software development using a team of AI agents.
See Issues, Pull Requests for supplemental documentation.

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

Six `.docx` files land flat in `outputs/`:

| File | Source |
|---|---|
| `Spring_2026_Performance_Objectives.docx` | Centerpiece overview |
| `Objective_1_Cross-Departmental_Capstone_Collaboration_Framework.docx` | Obj 1 detail |
| `Objective_2_Source_Control_Version_Control_Instructional_Modules.docx` | Obj 2 detail |
| `Objective_3_Ghost_Student_Discovery_Tool.docx` | Obj 3 detail (Ghost Tool / PM support) |
| `obj1_research_support.docx` | Obj 1 supporting research |
| `obj3_research_support.docx` | Obj 3 supporting research (ghost-student fraud brief) |

Internal-only docs (`inputs/# Purpose of work.md`, `inputs/raw_material/# PHILOSOPHICAL ISSUES.md`) are deliberately excluded — they are author scratchpads, not binder content.

### Reference doc (style consistency)

If a Word reference document exists at `inputs/design/binder-reference.docx`, the build picks it up automatically via pandoc's `--reference-doc=` flag, producing `.docx` output that conforms to the unified style set defined in [`inputs/design/Binder_Style_and_InDesign_Audit.md`](inputs/design/Binder_Style_and_InDesign_Audit.md).

If the reference doc is absent, the build falls back to pandoc's defaults so the designer has concrete output to react to on the first pass. Creating the reference doc is a follow-up once the designer settles on fonts (item 1 in the audit's "needing human judgment" list).
