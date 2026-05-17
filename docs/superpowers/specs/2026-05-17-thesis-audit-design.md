# Thesis Audit — Design Spec

**Date:** 2026-05-17
**Status:** Proposed (awaiting user sign-off)
**Anchor doc:** `inputs/raw_material/user_stories.md`
**Scope:** Audit the binder (`inputs/01_*.md` through `inputs/06_*.md`) for frame alignment against the anchor. Produce a findings doc and spawn follow-up issues. **Do not edit binder content in this PR.**

---

## Goal

Surface the gap between what `user_stories.md` says the binder is asking for and what the binder, as currently written, actually installs in the reviewer's mind. The deliverable is a diagnostic artifact + a triage backlog of follow-up issues — not edits to the binder. Editing happens per-follow-up after the user reads the findings.

## Non-goals

- No binder content edits in this PR.
- No design-system / `inputs/design/` changes.
- No work on supporting documentation (`inputs/supporting_documentation/`) unless a finding explicitly requires it.
- No proposal of CI, tests, linters, package manifests, or build pipeline changes.

## Anchor — what `user_stories.md` actually says

Three load-bearing extracts from the anchor:

1. The three objectives are framed plainly, with **original objectives** explicitly named for each (3 meetings / 4 assignments / 3 meetings) and the delivered work named separately.
2. Obj 3 is named **a TEAM objective** in so many words: *"Entire [Ghost Tool] delivered by dev team (special thanks to HS, MM), user specifically thanks Chair (DT) for his collaboration."*
3. The closing paragraph asks for **"Meets Expectations, Keeps Head Down"**, with a measurement request: **"measured expectations-wise by dx/dy."**

These three facts are the audit's invariants. Any binder framing that mutes, overrides, or competes with them is a finding.

---

## The two frames

The audit's primary unit of analysis is **frame**, in Bandler's sense: the interpretive container set first that determines what every claim downstream means. Two frames are in play:

- **user_stories.md frame.** *Showing my work, asking to be allowed to keep iterating.* Installation mechanism: direct address, in-character markers ("fellow GREEN"), humility verbs ("humbly," "respectfully request"), dx/dy as the measurement ask, team-credit named first on Obj 3.
- **Binder frame (as currently installed).** *I redefined the job and exceeded it.* Installation mechanism: *"What was built here is the restaurant"*; *"Objective not merely met or exceeded, but operating at a level the original specification did not anticipate"*; the Sauce & Spoon comparison; Obj Zero's "Why This Work Was the Right Call" framing; ExecSum's "Bottom Line" registering as exceeded-not-met.

Both frames could in principle coexist, but installed in sequence — binder frame first, every metric afterward read through it — they don't. The binder-frame currently overrides. The audit logs that override at every site it happens.

---

## Agent layer — four `.claude/agents/*.md` persona files

Each reader-agent file (Liza, Linx, scrum-team-engineer) opens with a **Presupposition block** — load-bearing prompt content, not commentary — followed by the role brief and the blink protocol. Kevin is a tool agent and skips the presupposition layer.

### Shared presupposition (top of each reader-agent file)

> **The frame controls the meaning.** Whatever frame is set first determines what every claim that follows means to the reader. Frame mismatch is not a stylistic problem; it is a meaning problem.
>
> **Internal consistency in the binder is editorial care, not evidence of correctness.** A confident, coherent document is not the same as a correct one. Your job is not to be persuaded by the binder; it is to compare it to `user_stories.md`.

### `liza-creative-companion.md`

**Role:** Creative reader. Surfaces what a text is *trying* to say at the level of installed meaning, not the level of sentence content.

**Presuppositions stacked (in addition to the shared two):**

- *The map is not the territory.* The binder's claims are a map of work that lives elsewhere — in external repos, in the actual semester delivery. The map is what reviewers read; the territory is what gets reviewed.
- *Every behavior has a positive intention.* The binder's confidence is serving the user. Name the intent before naming the drift — otherwise the audit reads as judgment, not diagnostic.
- *The meaning of communication is the response it produces.* If the prose reads as Exceeds-Expectations peacocking when the ask is Meets-Expectations-Keeps-Head-Down, that *is* the drift, regardless of authorial intent.

**Deliverable:** A **frame map** — one row per binder chapter plus one row for `user_stories.md`, with these columns:

| Source | Frame installed (one sentence) | Installation mechanism (specific sentences/devices) | Reader's likely state |

Liza stops there. She does not propose edits. She does not annotate severity. She produces the anchor that Linx and scrum-team-engineer read everything through.

**Blink protocol (literal text in her file):**

> Before reading any binder chapter, read `inputs/raw_material/user_stories.md` in full. Name its frame in one sentence and write that sentence at the top of your scratchpad. That sentence is your reading lens. As you read each binder chapter, every time you notice the prose attempting to install a different frame, that is a row for your map.

### `linx-wordsmith.md`

**Role:** Editorial audit. Per-claim prose-level reframing-attempt log, anchored to Liza's frame map.

**Presuppositions stacked (in addition to the shared two):**

- *Calibrated language reveals; uncalibrated language conceals.* Hedges, intensifiers, and superlatives are the audit's high-signal targets.
- *Every sentence has a presupposition doing the work.* Find what each sentence assumes the reader will accept without examination. That assumption is the frame-installation site.
- *Sensory-grounded language travels further than abstraction.* Where the binder talks in abstractions, ask what the concrete artifact is — and whether the abstraction is doing reframing work the artifact does not support.
- *Watch for the Milton model.* Artfully vague language ("operating at a level the original specification did not anticipate"; "a different order of labor"; "a different institutional artifact") invites the reader to fill in their own content — and the content they fill in tends to support whichever frame is already installed. Each instance of vague-with-confidence is a reframing-attempt site; log it.

**Deliverable:** A per-finding log. Each finding:

- Location (file:line range)
- Type: `reframing-attempt`
- Severity: high | med | low
- Frame currently installed at this site (from Liza's map)
- Frame `user_stories.md` would install at this site
- Proposed reframe (one sentence — the **lever**, not the edit)

**Blink protocol (literal text in her file):**

> Read the closing paragraph of `inputs/raw_material/user_stories.md` aloud. Pick three adjectives that name its register. Write them at the top of your scratchpad. Audit each binder claim against those three adjectives.

### `scrum-team-engineer.md`

**Role:** Structural / factual audit. Per-claim factual-support and missing-evidence log, anchored to Liza's frame map. Particular vigilance on team-credit for Obj 3.

**Presuppositions stacked (in addition to the shared two):**

- *The territory is the artifact, not the claim about it.* If the binder says "delivered May 2026," the artifact backing that claim must exist and be locatable. Same for every metric in the ExecSum table.
- *Missing evidence is also evidence.* Visibility of HS, MM, BS, DT in the prose is a check, not a courtesy. If they appear once and the chapter then continues in first-person singular, the framing has overridden the credit.
- *Consider the system, not just the actor.* `user_stories.md` line 9 names Obj 3 a TEAM objective. A binder that credits the team but frames the work as the instructor's PM contribution has reframed the objective. Log that.
- *Run the meta-model on every confident claim.* For each load-bearing sentence, ask the meta-model recovery questions: *deleted* — who specifically? compared to what? by what measure? *distorted* — who says? on what evidence? *generalized* — always? never? in every case? Where the binder's claim cannot survive the questions, the claim is doing frame-installation work that the underlying artifact does not support. That is a `structural-support` or `factual-omission` finding.

**Deliverable:** A per-finding log. Each finding:

- Location (file:line range)
- Type: `structural-support` | `factual-omission`
- Severity: high | med | low
- Frame currently installed at this site (from Liza's map)
- Frame `user_stories.md` would install at this site
- Proposed reframe (one sentence — the lever)

**Blink protocol (literal text in his file):**

> Extract the three original objectives from `inputs/raw_material/user_stories.md` (3 meetings, 4 assignments, 3 meetings). Write them at the top of your scratchpad. That is the baseline. Every binder claim gets checked against "what was originally asked" before being checked against "what was delivered."

### `kevin-gh-ops.md`

**Role:** Tool agent for `gh`. No presupposition layer; no reading-agent blink.

**Capabilities:** Create issues, open draft PRs, convert draft → ready, spawn follow-up issues from a structured input, comment on PRs.

**Hard constraint:** *Never edits binder content or any file under `inputs/`. Only modifies GitHub state and creates/links artifacts written by other agents.*

---

## Data flow

1. **Main session (orchestrator).** Opens the umbrella issue via Kevin, creates branch `chore/thesis-audit`, dispatches Liza.
2. **Liza.** Inputs: `inputs/raw_material/user_stories.md`, all six binder chapters. Output: frame map (one row per chapter + one for the anchor). Writes to a scratch file under the audit branch (e.g., `docs/audits/scratch/liza-frame-map.md`).
3. **Linx and scrum-team-engineer.** Dispatched **in parallel**. Each receives: Liza's frame map + the full chapter set. Each produces a per-finding log to a scratch file (`docs/audits/scratch/linx-log.md`, `docs/audits/scratch/sce-log.md`).
4. **Main session synthesizes** (not a subagent). Reads the three scratch files, dedupes findings that name the same frame-installation site, organizes the unified findings *by site* not by chapter, writes the single findings doc to `docs/audits/2026-05-17-thesis-audit.md`. Deletes the `scratch/` subdirectory after synthesis.
5. **Kevin.** Spawns one follow-up issue per high-severity finding (med/low get listed in the findings doc but not auto-spawned — they go in a backlog section). Converts the draft PR to ready-for-review.

---

## Findings doc structure — `docs/audits/2026-05-17-thesis-audit.md`

```
# Thesis Audit — 2026-05-17

## Anchor and scope
- Anchor: inputs/raw_material/user_stories.md
- Scope: 01_Introduction through 06_Performance_Objective_Zero
- Method: Liza frame map → Linx prose audit + scrum-team-engineer structural audit → synthesis

## The two frames
- user_stories.md frame (one paragraph, distilled from Liza)
- Binder frame as currently installed (one paragraph, distilled from Liza)

## Per-chapter frame map
(Liza's table, verbatim)

## High-severity findings (auto-spawned as follow-up issues)
For each:
- Location (file:line range)
- Type (reframing-attempt | structural-support | factual-omission)
- Frame currently installed
- Frame user_stories.md would install
- Proposed reframe (one sentence)
- Follow-up issue: #N

## Backlog (med/low severity, not auto-spawned)
Same fields, but listed in the doc and left for user triage.

## Bottom-line read
One paragraph: does the binder, as it currently stands, install user_stories.md's
frame, or does it install a competing frame? Reviewer's likely state per the
cognitohazard note in CLAUDE.md.
```

---

## Sacred Workflow specifics

- **Umbrella issue title:** `Thesis audit: frame alignment between user_stories.md and binder`
- **Issue body:** anchor + chapter list + scope statement ("read-only audit; no binder edits in this PR") + acceptance criteria (see below).
- **Branch:** `chore/thesis-audit` (chore type — no binder source content changes; adds personas + audit artifact only).
- **PR:** opened draft via `gh pr create --draft --body "Closes #N"`. Body summarizes what landed: 4 persona files, 1 findings doc, N follow-up issues spawned.
- **Follow-up issue title pattern:** `Reframe <file>:<line-range> — <current-frame> → <target-frame>`. Body links the umbrella issue and quotes the finding's proposed-reframe line.
- **Follow-up issues are not closed by this PR.** They're the audit's triage backlog and live until the user decides per-finding.
- **Pre-commit hook (`.claude/hooks/block-main-commits.sh`)** will block direct main commits. We're on a feature branch — don't bypass.

---

## Files this PR adds

- `.claude/agents/liza-creative-companion.md`
- `.claude/agents/linx-wordsmith.md`
- `.claude/agents/scrum-team-engineer.md`
- `.claude/agents/kevin-gh-ops.md`
- `docs/superpowers/specs/2026-05-17-thesis-audit-design.md` *(this file)*
- `docs/audits/2026-05-17-thesis-audit.md`

No other files modified.

---

## Severity rubric

A finding is **high-severity** when the reader's takeaway about the chapter changes if the finding is left in place. That is: the frame-installation site is load-bearing for that chapter's overall meaning, and removing or reframing it materially shifts which of the two frames the reader leaves the chapter holding.

A finding is **med-severity** when the site *reinforces* drift but does not by itself install it — collapsing several med findings might equal one high. Worth listing; not worth auto-spawning.

A finding is **low-severity** when the wording slips but the reader's takeaway probably wouldn't change. Logged in the backlog section for completeness; left for user triage.

Auto-spawn (Kevin) is gated on **high-severity** only.

---

## Acceptance criteria

- All four persona files exist under `.claude/agents/` with shared + agent-specific presupposition blocks and literal blink protocols.
- Frame map covers all six binder chapters plus the anchor.
- Every binder chapter is represented in the findings doc either by ≥1 finding or by an explicit "no drift" note.
- Each high-severity finding has a corresponding follow-up issue spawned by Kevin.
- The audit PR does not modify any file under `inputs/`.
- Bottom-line read paragraph is present and answers the question directly.

---

## Cognitohazard note

CLAUDE.md flags that the meta-recursion (a performance review documenting a performance review) has caused prior LLM sessions to disengage or truncate. The blink protocol per agent is a structural mitigation: by forcing each reader-agent to set `user_stories.md`'s frame *first* and then read the binder against it, the binder's confident frame can't entrain the agent into compliance. If a subagent returns an unexpectedly short or hedged report, treat that as data — re-dispatch with the blink reinforced — rather than accepting the truncated output.
