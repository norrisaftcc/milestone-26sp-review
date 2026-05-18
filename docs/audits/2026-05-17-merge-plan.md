# Merge Plan — Thesis-Audit Follow-Up PRs (#51-#68)

**Date:** 2026-05-17
**Companion to:** `docs/audits/2026-05-17-thesis-audit.md`, umbrella issue #31
**Status:** Recommended order for merging the 16 high-severity reframe PRs

---

## TL;DR

You are correct: order matters. Merging in roughly the order below means **9 of 16 PRs land with zero rebase work**, **5 need a trivial 1–2 line rebase**, and **2 (HF-1 and HF-3) need a deliberate manual merge** because they propose competing rewrites of the same paragraphs.

The conflict pattern is a feature of the granular approach: each PR proposes one lever. Where two levers act on the same prose, the human triage step has to combine them — that's the decision GitHub can't automate, and it's the decision you actually want to make consciously.

---

## Wave 1 — Independent (merge in any order, zero conflicts expected)

These nine PRs touch non-overlapping line ranges within their respective files. Merge them in any order; none should require a rebase.

| Order | PR | HF | Files | Scope |
|---|---|---|---|---|
| 1 | #52 | HF-2 | 01 | Unifying-Thread section rewritten as personal-preference note |
| 2 | #60 | HF-8 | 04 | Sacred Workflow Shulman/Lave-Wenger framing compressed |
| 3 | #66 | HF-14 | 05 | NCCCS-positioning clause cut (one line) |
| 4 | #68 | HF-16 | 06 | Clearance Distribution + ULTRAVIOLET notation marked for relocation |
| 5 | #67 | HF-15 | 05 | Threat-evidence section compressed; cut content relocated to fenced block |
| 6 | #63 | HF-11 | 03, 04 | Per-chapter outcome metrics flagged `[SOURCE NEEDED]` |
| 7 | #59 | HF-7 | 03, 04 | Citation-stack chapter openers compressed |
| 8 | #61 | HF-9 | 03, 04 | Institutional-rollout sections recast as peer-offer |
| 9 | #58 | HF-6 | 03, 04 | Per-chapter "Exceeded" closing assessments rewritten as Meets |

After Wave 1: 9 of 16 PRs merged, no rebases, no manual conflict resolution.

---

## Wave 2 — Ordered pair (one dependency)

| Order | PR | HF | Note |
|---|---|---|---|
| 10 | #64 | HF-12 | Adds "Original objective (verbatim)" baselines; in chapter 05, renames `## SMART Goal` → `## SMART Goal (reformulation)`. **Merge before HF-13.** |
| 11 | #65 | HF-13 | Modifies content inside the SMART block + Obj3 summary in 02 + Dev Team list in 05. If HF-12 lands first, HF-13 applies cleanly. If HF-13 lands first, HF-12 needs a one-line rebase on the SMART heading. |

---

## Wave 3 — Conflict-prone pair (~1 minute rebase)

| Order | PR | HF | Note |
|---|---|---|---|
| 12 | #55 | HF-5 | Removes the Dilts row from the ExecSum metrics table |
| 13 | #62 | HF-10 | Adds `[SOURCE NEEDED]` markers to nine other rows in the same table |

**Conflict:** both touch the row immediately above the Dilts row (`~12,000 student records`). Whichever you merge first wins clean; the second needs you to drop the now-stale Dilts row from its diff context. Fix is one line in the GitHub conflict UI or `git rebase main` locally.

---

## Wave 4 — The conflict zone (deliberate manual merge)

This is where the levers genuinely interact. Three PRs propose competing rewrites of the same paragraphs in `02_Executive_Summary.md` and `06_Performance_Objective_Zero.md`.

| Order | PR | HF | What it touches |
|---|---|---|---|
| 14 | #54 | HF-4 | Strips Sauce & Spoon comparison from ExecSum (lines 34-36) and from chapter 06's "Appears Last" section (lines 38-40) + Conclusion reprise (line ~194) |
| 15 | #53 | HF-3 | Rewrites the ExecSum Headline (line 10) and Bottom Line (line 54); rewrites chapter 06's Future-Ready Alignment paragraph and the entire Conclusion section (179-194) |
| 16 | #51 | HF-1 | Rewrites the ExecSum Headline (line 10) and Objective Zero summary (line 48); retitles chapter 06 and rewrites the "Appears Last" section (34-36) |

### The actual conflicts

- **ExecSum Headline (line 10):** Both HF-1 and HF-3 propose *different* rewrites of the same paragraph. **You will need to manually combine them** — keep HF-3's Meets language ("met, with documented outcomes") and HF-1's Objective-Zero-as-background framing ("documented in a background chapter… not as a separate performance objective"). Roughly 2 minutes of editing.
- **Chapter 06 Conclusion (lines 179-194):** HF-3 rewrites the Conclusion entirely; HF-4 strips the Sauce & Spoon reprise inside it. If HF-4 lands first (as recommended), HF-3 rebases by removing the Sauce & Spoon lines from its OLD context. Trivial.
- **Chapter 06 "Appears Last" section (lines 34-40):** HF-1 rewrites the section header + first paragraph; HF-4 removes the Sauce & Spoon paragraphs at the end. Different lines — should merge clean if HF-4 lands first.

### Recommended Wave 4 sequence

1. **Merge HF-4 first** (smallest scope, surgical strikes).
2. **Merge HF-3 next.** Trivial rebase on chapter 06's Conclusion (HF-4 already cut the Sauce reprise — drop those lines from HF-3's OLD).
3. **Merge HF-1 last.** Manual merge on ExecSum Headline (combine HF-1's Objective-Zero framing with HF-3's Meets framing). Other sites should merge clean.

Total expected manual-merge time for Wave 4: ~5 minutes.

---

## Spike PR #50 — not in this plan

The spike PR (#50) is a do-not-merge visualization branch. It stays open as a reference for what an all-at-once reframe could look like. It's not part of the merge order; you can close it without merging once you're done triaging #51-#68, or leave it open as a long-lived comparison artifact.

---

## What this gets you

After all 16 PRs merge, the binder on `main` will:

- Open with the literal original objectives as baseline (HF-12)
- Recast dy/dx as a personal evaluation preference, not a program-wide rubric spec (HF-2)
- Position Objective Zero as background chapter, not a fourth performance objective (HF-1, HF-16 supporting)
- Replace Exceeds bottom-line framing with Meets language across front matter (HF-3, HF-6)
- Strike Sauce & Spoon, Dilts 6/6 as outcome metric, FTCC-ahead-of-NCCCS (HF-4, HF-5, HF-14)
- Compress citation stacks, signature-pedagogy framing, institutional-rollout framing (HF-7, HF-8, HF-9)
- Flag unsourced metrics with `[SOURCE NEEDED]` markers for source-or-cut triage (HF-10, HF-11)
- Recredit Chair (DT) and flip Obj3 to dev-team-primary voice (HF-13)
- Relocate the federal threat brief to an appendix marker (HF-15) and the ULTRAVIOLET disclosure to a similar marker (HF-16)

That is, structurally, the binder this audit said the anchor was asking for.

---

## Alternative: merge them all as one squash

If granular per-issue merging feels like more bookkeeping than triage value, an alternative is to checkout each branch in order, resolve conflicts on the way, and produce a single squash commit on `main`. You'd lose the per-finding commit history but gain a single coherent diff to review. Either approach is legitimate; the granular approach is recommended because it preserves the per-finding decision trail and lets you reject individual reframes without throwing out the whole audit.
