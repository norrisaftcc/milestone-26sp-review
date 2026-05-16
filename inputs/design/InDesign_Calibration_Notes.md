# InDesign Calibration Notes

Calibration pass between the designer's published InDesign draft and the unified style spec proposed in `inputs/design/Binder_Style_and_InDesign_Audit.md`. The draft was published from the **pre-revision Objective Zero** source — content drift relative to the current markdown is expected and out of scope. The concern here is the typographic system and the aesthetic decisions in evidence.

---

## What was examined

- **Initial URL fetch:** `https://indd.adobe.com/view/6417c5ce-56af-4640-bb9e-0fb04a185aec`. Adobe Publish Online is a JavaScript SPA; the viewer chrome renders page imagery into a canvas after page load. WebFetch returned only the literal string `Publish Online` — no design content was scrapable from the URL.
- **PDF export provided:** Subsequent to the initial fetch, the designer made the InDesign output available as a PDF at `inputs/design/SAMPLE_OUTPUT/AF_PerformanceObjective_Report.pdf` (12 pages, 524KB). The findings below are drawn from that PDF — full text content extracted via PDFKit's `attributedString` API; embedded font descriptors extracted from the PDF's font catalog.
- **Still not directly extractable without page-rendering tools (`pdftoppm` / image renderers):** color values used in the layout, exact paragraph spacing in points, baseline-grid behavior, the visual treatment of tables and callouts. Items requiring visual confirmation are flagged inline below.

---

## Aesthetic choices in evidence

### Font system in use (extracted from embedded font descriptors)

| Role in draft | Font family | Weights / variants present |
|---|---|---|
| **Display / heading hierarchy** | **Magistral** (Paratype, Adobe Typekit-available) | Book (400), Medium (500), Bold (700), ExtraBold (800), Book Italic, Medium Italic, Bold Italic, plus a Condensed Book |
| **Body copy** | **Kallisto** (Hannes von Döhren / ITC) — **a serif** | Light (300), Medium (500), Bold (700), Heavy (900), Medium Italic, Bold Italic, Heavy Italic |
| **Monospace** | **Courier Prime** | Regular |
| **Wordmark / brand chrome** | **Ethnocentric Rg-Regular** | Regular |
| **Decorative accent** | **Thirsty Script Regular** | Regular |

All five families are embedded as subsetted PDF fonts (`FontFile2` / `FontFile3` with `ToUnicode` mappings), confirming the designer has live workstation access to them — almost certainly via Adobe Fonts / Typekit kit `qng8dvy`. **These are very likely the "AF brand fonts" the author flagged as forthcoming.**

### Page structure (from text extraction)

- 12 pages emitted from the pre-revision Objective Zero source (which is one chapter; the binder build emits a 6-row table to one `.docx`, so InDesign is expanding the page count via layout).
- **Cover (page 1)** — `AlgoCratic Futures™ · Immersive Learning Experience` wordmark; `ALGOCRATIC FUTURES™ · INSTITUTIONAL EFFECTIVENESS DIVISION` strap; title `CITIZEN PERFORMANCE TRAJECTORY ANALYSIS · Performance Objective Zero`.
- **Divider (page 2)** — sole content: the tagline `The Algorithm provides. Everything you need. Nothing you want.`
- **Body pages (3–11)** with the per-page footer rhythm:
  - Even pages: `The Algorithm provides. Everything you need. Nothing you want.`
  - Odd pages: `All paths lead to optimization. Even the wrong ones. Especially the wrong ones.`
- **Page 12** — appears blank in text extraction (`undefined` returned). Likely a back cover or end plate.
- **Section heading style**: ALL CAPS sub-heads (`LEVEL 1: ENVIRONMENT — WHERE DOES THIS HAPPEN?`, `LEVEL 2: BEHAVIOR — WHAT IS REQUIRED, SPECIFICALLY?`, etc.; also `REPLICABLE INFRASTRUCTURE`, `FUTURE-READY ALIGNMENT`).

### In-character vocabulary preserved

All of the following are verbatim in the PDF text:

- `Sacred Workflow™` (with trademark mark, including the seven-stage `Issue → Branch → Draft PR → Code/Test → Finish PR → Review → Merge` formula on page 6).
- `ULTRAVIOLET-Adjacent` notation block on page 3, intact with the `frotz` Easter egg and the closing `The Algorithm is aware. The Algorithm approves. The Algorithm, in this context, is you.` line.
- Document Clearance Distribution: BLUE (Department Chair) · INDIGO (Division Dean) · VIOLET (C-Suite Administration) · ULTRAVIOLET ([REDACTED]). Note: "Department Chair" / "Division Dean" — slightly more institutional than the source's "Chair" / "Dean".
- Pull quotes formatted as set-apart blocks: the "filter will win" architecture-not-motivation quote on page 4; the "Measuring y vs. dy/dx" quote on page 7.
- Citations preserved with italic title formatting in evidence (Dweck, Edmondson, Lave & Wenger).

### GRAY vs GREY — designer's correction partially applied

The PDF carries both spellings:

- **Page 8 Key Deliverables table**: `GRAY Clearance instructional design onboarding brief` (post-correction).
- **Page 10 Conclusion bullet**: `Cross-disciplinary collaboration framework built on the GREY clearance model (Objective 1)` (pre-correction — missed).

Either the designer's InDesign source was partially updated, or the PDF predates a final reconciliation pass. Flagging for the next revision.

---

## Comparison against the audit's unified style spec

| Audit recommendation | Verdict | Evidence / next step |
|---|---|---|
| Three character styles (`Strong`, `Emphasis`, `Code`, `Hyperlink`) | **Unknown** | Text extraction does not reveal character-style names; needs InDesign panel access. |
| Six-token color palette (`ink` / `rule` / `muted` / `paper` / `accent-indigo` / `accent-gray`) | **Unknown** | Color values not directly extractable without page-rendering tools. Author should confirm visually. |
| Font assignment — Body = Exo Regular 10.5pt | **Diverge** | Body is **Kallisto** (a serif), not Exo (a sans). Designer's call — see below. |
| Font assignment — Heading 1 = Goldman Bold | **Diverge** | Headings use **Magistral** (geometric sans by Paratype), not Goldman. This answers prior blocking question #1. |
| Font assignment — Heading 2 / 3 = Exo same-family as body | **Diverge** | Heading family (Magistral) and body family (Kallisto) are *different families* — opposite of the audit's same-family recommendation. Likely intentional sans/serif contrast. |
| Font assignment — Callouts = IBM Plex Mono | **Diverge** | Monospace voice uses **Courier Prime** throughout, not IBM Plex Mono. The audit had reserved Courier Prime for distinctive in-character moments; designer promoted it to the routine monospace face. |
| Font assignment — Captions / footers = Exo Regular 8–9pt +20 tracking | **Unknown** | Visual confirmation of size/tracking needed. Footer text is present and consistent across pages. |
| Restraint to three heading levels actually applied | **Likely diverge** | At least four typographic tiers in evidence (cover title, chrome header, body H1, ALL-CAPS sub-head, body) before counting pull quotes and footer chrome. Confirm via InDesign panel. |
| Clearance-frame aesthetic preserved (INDIGO color-block / classification banner) | **Likely confirmed** | The Document Clearance Distribution block on page 3 reads as a deliberately framed unit; visual confirmation needed for the exact treatment. |
| INDIGO chrome as styled text frame, *not* anonymous imported Word tables | **Likely confirmed** | PDF text reads cleanly without table-cell artifacts in the clearance distribution treatment, suggesting the designer rebuilt it natively in InDesign rather than importing the source `.docx`'s table version. |
| Hyperlinks in `rule` color, not Word default `#0563C1` | **Unknown** | No hyperlink targets visible in extracted text. |
| AlgoCratic Futures in-character apparatus preserved as load-bearing | **Confirmed** | Sacred Workflow, clearance levels, ULTRAVIOLET-Adjacent "frotz" notation, Algorithm-is-you closing — all intact. The framing is honored, not stripped. |
| GRAY clearance spelling (post-correction) | **Partial** | Page 8 correct; page 10 still uses "GREY". Designer's correction needs another pass. |

---

## Calibration items

### Calibrate the source side

The designer has made a coherent set of typographic choices visible in the PDF. The source-side priority is to land a `binder-reference.docx` that maps onto those choices so the `.docx` exports stop fighting the InDesign design:

1. **Build `inputs/design/binder-reference.docx` against the designer's font system, not the audit's original recommendation.** Concretely:
   - Body = **Kallisto** Light or Medium for body, Bold for inline emphasis.
   - Heading 1 = **Magistral** Bold or ExtraBold.
   - Heading 2 / Heading 3 = **Magistral** Medium or Book.
   - Callout / Code = **Courier Prime** Regular.
   - Wordmark / chrome = **Ethnocentric** (reserved for AlgoCratic Futures brand moments).
   - Adobe Fonts / Typekit activation required on whichever workstation runs the `.docx` -> InDesign import (the same `qng8dvy` kit the author flagged).
2. **Collapse PerfZero v2's source-side 22-color palette to the unified six tokens** even before color values are confirmed against the InDesign draft. This is the highest-leverage single source-side change and was the audit's headline finding; it remains true regardless of which colors the designer ultimately chose.
3. **Heading-level reconciliation**: PerfZero v1 vs. v2 disagree on whether the top-level head is `Heading1` or `Heading2`. Reference doc should pin one answer.
4. **Standardize inline code via a named `Code` character style** so paths and command names emit via style rather than direct `<w:rFonts w:ascii="Consolas">` runs.
5. **Reproduce the clearance-frame aesthetic as styled paragraph + color block at the markdown level** (probably via a pandoc filter or template div) rather than the current anonymous Word tables, so the InDesign import does not need rebuild work every cycle.
6. **Footer convention**: pin one classification-line + page-number pattern, with classification text varying per document.

### Calibrate the InDesign side

1. **Reconcile the GRAY / GREY discrepancy on page 10.** Page 8 already uses GRAY; page 10 still uses GREY. Fix in the InDesign source before the next export.
2. **The audit's "same family for body and headings" recommendation needs to be retired** — designer's call to use **Magistral (sans) + Kallisto (serif)** is a meaningful aesthetic decision and the contrast is doing visible work. The audit should be updated to record this divergence as accepted, not pushed back.
3. **Color palette confirmation pass**: with the InDesign source open, count distinct colors actually in use in body content (excluding clearance-frame moments). If the count is more than ~6, collapse to the unified set.
4. **Heading-level audit**: confirm the document uses at most three heading levels (H1, H2, H3) plus the ALL-CAPS sub-head. If the ALL-CAPS treatment is doing the same job as a heading level, it should be a named paragraph style, not direct formatting.

### Unresolved / requires visual or InDesign-panel access

- Exact color values in use (six tokens or more?).
- Exact paragraph style names in InDesign (`Heading 1` matching the audit's recommended naming, or something native to InDesign?).
- Paragraph spacing / leading in points.
- Whether tables (the Dilts six-level table on page 6, the Key Deliverables table on page 8) use a single named table style or are anonymous one-offs.
- Whether the ALL-CAPS sub-head treatment is a named paragraph style or a transform applied to `Heading 2`.

Each of these is a one-screenshot-from-the-designer answer; none blocks the next source-side step.

---

## Reference doc (binder-reference.docx) readiness

**Verdict: yes, buildable now.** The earlier "partial / not yet" call rested on two open font variables. Both are resolved by the PDF:

- The Adobe Typekit kit `qng8dvy` is the route the designer is using — Magistral, Kallisto, Courier Prime, Ethnocentric, Thirsty Script are all activated on the designer's workstation, embedded as subsets in the PDF.
- The "AF brand fonts" the author flagged as forthcoming are very likely this same kit. There is no separate kit pending delivery that would invalidate the font choice on next arrival.

The next step is mechanical: build `inputs/design/binder-reference.docx` in Word against this font system, commit it, and the existing `scripts/build_binder.sh` picks it up automatically on next run. Anyone running the build needs to either have those Adobe Fonts activated locally or have the Google-Fonts fallback set installed (Courier Prime is on Google Fonts; Magistral and Kallisto are paid Adobe Fonts and would substitute on machines without Typekit access). For author/build-machine use a documented font fallback chain in the reference doc.

---

## Recommended next handoff

The 30-minute working session previously recommended now has a sharper agenda — most of the typography is settled and visible. Take to the designer with the `.indd` open on screen:

1. **Page 10 GRAY/GREY fix** — confirm and apply.
2. **Color values** — read off the actual hex codes in use for body ink, rule, muted, paper, and the clearance accent palette. Update the source-side `binder-reference.docx` and audit accordingly.
3. **Paragraph style names** — are they named in InDesign as `Heading 1` / `Heading 2` / `Heading 3` (matching what pandoc will emit) or as `Section Head` / `Subhead` etc.? If the latter, set up a Word-to-InDesign style mapping preset once.
4. **The Magistral + Kallisto pairing**: confirm the audit's "same family for body and headings" recommendation is retired in favor of the deliberate sans/serif split.
5. **Courier Prime usage scope**: confirm the audit's "Courier Prime reserved for distinctive in-character moments" is retired in favor of Courier Prime as the routine monospace voice. (If so, the audit's IBM Plex Mono recommendation can be dropped.)

After this session, the reference doc can be committed, the source `.docx` files can be regenerated against it, and the next InDesign import cycle has no avoidable surprises.
