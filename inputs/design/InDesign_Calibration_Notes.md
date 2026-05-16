# InDesign Calibration Notes

Calibration pass between the designer's published InDesign draft and the unified style spec proposed in `inputs/design/Binder_Style_and_InDesign_Audit.md`. The draft was published from the **pre-revision Objective Zero** source — content drift relative to the current markdown is expected and out of scope. The concern here is the typographic system and the aesthetic decisions in evidence.

---

## What was examined

- **URL accessed:** `https://indd.adobe.com/view/6417c5ce-56af-4640-bb9e-0fb04a185aec`
- **Also attempted:** `https://indd.adobe.com/embed/6417c5ce-56af-4640-bb9e-0fb04a185aec` and `https://indd.adobe.com/api/v1/documents/6417c5ce-56af-4640-bb9e-0fb04a185aec` (404).
- **What WebFetch actually returned:** the literal string `Publish Online` and nothing else. The Adobe Publish Online viewer is a client-rendered single-page application — the document pages are loaded into a canvas/image viewer by JavaScript after page load and are not exposed in the initial HTML payload. No document text, no font references in CSS, no image asset URLs, no metadata fields, and no aria/alt text describing pages were retrievable.
- **Net inferable from the fetch:** essentially nothing about the design. The fetch confirms only that the URL is live and serves Adobe's Publish Online viewer chrome.

**This calibration is therefore performed against the audit spec only**, with explicit flags throughout for every item that requires the author to open the InDesign draft in a browser and confirm or deny visually. Findings phrased as "the draft does X" below are conditional on visual confirmation by a human reviewer; they are framed as questions to be answered, not assertions about what is on the page.

---

## Aesthetic choices in evidence

**Not determinable from the fetched payload.** The Publish Online viewer serves rendered page imagery via JavaScript; the raw HTML carries no document content, no embedded fonts, no CSS color tokens, and no page count.

To proceed, the author should open the link in a browser and, page by page, fill in the table in the next section. The categories the audit cares about — and that this calibration would have populated if the content were scrapable — are:

- **Layout grid:** single- vs. multi-column; margins; presence of a baseline grid visible at headings.
- **Color palette in use:** is the body chrome the unified `ink` / `rule` / `muted` set (`#1A2332` / `#2B4C6F` / `#595959`) plus paper, with `accent-indigo` / `accent-gray` reserved for clearance framing? Or is the wider PerfZero v2 palette in evidence?
- **Typographic hierarchy:** are at most three heading levels visible? Do Heading 1 and Heading 2 read as different *faces* (Goldman vs. Exo) or only as different *sizes* of the same face?
- **Banner / callout treatments:** is there a dedicated Sacred Workflow / in-character callout style (monospace, left rule, indented), or are callouts handled as inline bold/colored body text?
- **Clearance-frame aesthetic:** does the INDIGO-style top color block / classification banner appear as a styled text frame with a color block (the audit's recommended technique), or does it import as a Word-style anonymous table?
- **Table styling:** is there a single named table style, or are tables visually inconsistent across pages?
- **Header / footer chrome:** one classification line + page number, applied uniformly? Or do per-document footers from the four source `.docx` files persist in unreconciled forms?

---

## Comparison against the audit's unified style spec

Confirmation requires visual inspection of the published view. The table below lists what to look for and the verdict the author should record after viewing the draft.

| Audit recommendation | What to look for in the InDesign draft | Verdict (to be filled in on visual inspection) |
|---|---|---|
| Eight paragraph styles (`Normal`/`Body`, `Heading1`, `Heading2`, `Heading3`, `BulletList`, `NumberedList`, `Callout`, `Caption`) | At most ~8 distinct paragraph treatments visible; specifically a dedicated `Callout` (monospace, ruled) and `Caption` (small, tracked) | Silent (not determinable from fetch) |
| Three character styles (`Strong`, `Emphasis`, `Code`, plus `Hyperlink`) | Inline code in IBM Plex Mono at ~95% body size; hyperlinks in `rule` color (`#2B4C6F`), not Word's `#0563C1` | Silent (not determinable from fetch) |
| Six-token color palette (`ink`, `rule`, `muted`, `paper`, `accent-indigo`, `accent-gray`) | No more than six distinct colors across body content; brand violets used only for INDIGO clearance frames | Silent (not determinable from fetch) |
| Font assignment — Body = Exo Regular 10.5pt | Body copy reads as Exo, not Arial or Calibri | Silent (not determinable from fetch) |
| Font assignment — Heading 1 = Goldman Bold 24pt | Chapter titles render in a wedge-serif display face (Goldman) rather than a sans | Silent — and this is the open question flagged in audit item #1 |
| Font assignment — Heading 2/3 = Exo Bold / SemiBold | Section / subsection heads in the same family as body, only weight changes | Silent (not determinable from fetch) |
| Font assignment — Callouts = IBM Plex Mono | Sacred Workflow / in-character callouts in a monospaced face | Silent (not determinable from fetch) |
| Font assignment — Captions, footers, classification banners = Exo Regular 8–9pt with +20 tracking | Footer / classification chrome reads as deliberate UI chrome, not body text shrunk down | Silent (not determinable from fetch) |
| Restraint to three heading levels actually applied | Document uses H1/H2/H3 only; no Heading 4–6 in evidence | Silent (not determinable from fetch) |
| Clearance-frame aesthetic preserved (visual outcome from INDIGO brief) | Color-block + classification-line treatment present at appropriate moments | Silent (not determinable from fetch) |
| INDIGO chrome implemented as styled text frame, *not* imported anonymous Word tables | No tell-tale Word-table cell-border artifacts; clean color blocks; consistent inset | Silent (not determinable from fetch) |
| Hyperlinks in `rule` color (`#2B4C6F`), not Word default `#0563C1` | Link color matches the rule color, not bright Office blue | Silent (not determinable from fetch) |
| AlgoCratic Futures in-character apparatus (clearance levels, Sacred Workflow stages, GRAY-clearance designation) treated as load-bearing | These terms appear in the layout with deliberate type-system support (e.g., monospace callout boxes, distinct color tags), not stripped or normalized into generic body prose | Silent (not determinable from fetch) — **flag if visibly stripped, this is non-negotiable per CLAUDE.md** |

---

## Calibration items

### Calibrate the source side

The following are concrete changes the markdown / `.docx` pipeline should adopt **before** the next InDesign import cycle, regardless of what the current draft looks like. These are recommendations the audit already makes; they are repeated here because they are the prerequisites for the InDesign side to converge:

1. **Introduce `inputs/design/binder-reference.docx`.** Until this exists, every pandoc export will re-emit duplicate `Heading1/2/3` definitions, an empty `fontTable.xml`, and run-level `rPr` overrides on every heading. InDesign cannot map what arrives malformed.
2. **Standardize the base font in the reference doc.** Whether the answer is Exo (current audit recommendation) or an as-yet-undelivered AF brand body face, the four source documents need to agree. Today, Spring is Calibri and the three raw_material docs are Arial.
3. **Collapse heading levels to three.** Remove `Heading4`–`Heading6` from the reference doc; reconcile PerfZero v1's use of `Heading2`-for-top-level vs. v2's `Heading1`.
4. **Define a single inline-code path.** Add a `Code` character style to the reference doc so inline code, file paths, and command names emit as a named style rather than raw `<w:rFonts w:ascii="Consolas">` runs.
5. **Cut PerfZero v2's color palette to the six-token set.** This is the highest-impact single source-side change. 22 colors collapsing to six will dominate the visual impression of the rebuilt draft far more than any font swap.
6. **Reproduce the INDIGO clearance frame as a styled paragraph + color block, not as nested tables.** This is a markdown-level change (probably a fenced `:::` div with a known class that the reference doc styles) plus a pandoc filter or template entry. Until this happens, InDesign will keep receiving anonymous Word tables for the institutional banner aesthetic.
7. **Pin a uniform footer convention.** One classification line + page number, with the classification text varying per document. Footer face = Exo (or AF body face) Regular 8pt with +20 tracking.

### Calibrate the InDesign side

These are items the audit's spec is confident about and that the next revision of the InDesign draft should adopt:

1. **Three heading levels, not four+.** If the current draft uses more, collapse.
2. **Map hyperlinks to a `rule`-colored character style**, not the imported Word default `#0563C1`.
3. **Replace anonymous imported tables with a single named "Body Table" object style.** Save once as an Import Options preset so subsequent `.docx` places are consistent.
4. **Define `Callout` as a dedicated paragraph style** (IBM Plex Mono, left rule, indent) and use it for Sacred Workflow stages and in-character pedagogy moments. If the current draft is rendering callouts as inline bold body text, this is the single biggest tonal upgrade available.
5. **Reserve brand violets for clearance frames only.** If `accent-indigo` is appearing in body decoration, pull it back to the classification-banner moments. The "clearance palette stays out of body content" rule is the audit's load-bearing color discipline.
6. **Preserve AlgoCratic Futures vocabulary verbatim.** Per CLAUDE.md, terms like "GRAY clearance," "YELLOW exit tickets," "Sacred Workflow," and the clearance hierarchy are load-bearing pedagogy. If the InDesign treatment normalizes these into generic body prose (e.g., un-stylizing "GRAY clearance" to "gray clearance" lowercase, or stripping the typographic distinction between clearance tags and surrounding text), the next revision should restore the deliberate treatment.

### Unresolved / requires direct access

The published Publish Online URL does not expose any of the following without a human visually inspecting the draft, or — for full certainty — direct access to the `.indd` source file:

- **Exact paragraph style names in InDesign.** Whether the designer is using `Heading 1` / `Heading 2` / `Heading 3` (matching the audit's recommended names, which map cleanly from pandoc's output) or InDesign-native names like `Section Head` / `Subhead` that will need an explicit Word-to-InDesign style mapping at every future import.
- **Exact font weights and sizes in use.** The audit specifies Goldman Bold 24pt / Exo Bold 15pt / Exo SemiBold 11.5pt / Exo Regular 10.5pt. The draft may be using different weights or sizes; only the `.indd` source will confirm.
- **Paragraph spacing in points.** Before/after spacing, leading, keep-with-next behavior on headings.
- **Whether Adobe Fonts (Typekit kit `qng8dvy`) is activated on the designer's workstation and which faces from that kit are actually placed.** This matters because Typekit faces cannot ride along in the `.docx` files; if the designer is using Typekit faces in InDesign that don't have Google Fonts equivalents on the markdown side, the binder will look one way in the InDesign draft and another way in any `.docx` preview.
- **Table style names and object style names.** Whether there is a single "Body Table" object style or whether every table is anonymous (replicating the source-side problem one level downstream).
- **Whether the AF brand fonts have been delivered to the designer.** The notes file describes these as forthcoming "install files." Their arrival is a precondition for the Heading 1 / display-face decision.

These items cannot be settled by a published-view inspection. They require either a screen-share walkthrough of the `.indd` with the designer, or an export of the InDesign paragraph/character/object style panels as a screenshot or text dump.

---

## Reference doc (binder-reference.docx) readiness

**Verdict: not yet — partial at best.** Audit item #1 under "Items needing human judgment" makes the reference doc contingent on the font choice settling. From what this calibration can determine:

- The Google Fonts list (Exo, Goldman, IBM Plex Mono, Courier Prime) is locally installable and stable enough to commit a reference doc against.
- However, the author has explicitly flagged two open variables: (a) the Adobe Typekit kit `qng8dvy` as "better fonts" the author would prefer if they could be made to work, and (b) an undelivered AF brand font kit with a style guide. Either of these arriving would invalidate the Heading 1 / display role choice (and possibly the body face choice) in a reference doc built today.
- The published InDesign draft is the one piece of evidence that could tell us whether the designer has *de facto* settled the question by committing to a specific display face in the layout. The Publish Online URL does not expose that information to scraping, and this calibration cannot confirm or deny it.

**Recommendation:** Do not commit `binder-reference.docx` until either (a) the author rules out Adobe Typekit and the AF brand kit as binder-pipeline fonts, accepting Exo / Goldman / IBM Plex Mono as the committed set; or (b) the AF brand kit arrives. Building the reference doc now and rebuilding it on AF-kit delivery is wasted motion and will produce a phantom `.docx`-style drift between the pre-AF and post-AF exports.

Acceptable interim move: commit a `binder-reference-DRAFT.docx` clearly marked as provisional, run all four `.docx` regenerations against it, and accept that the next AF-kit delivery will require one rebuild. This is the right call if the author wants InDesign import discipline *now* and is willing to absorb one re-import cycle later.

---

## Recommended next handoff

**Schedule a 30-minute working session with the designer where the `.indd` source is open on screen.** The author should walk the designer through the audit's eight-paragraph / three-character / six-color spec and the two of them should jointly answer: (1) which display face is in use for Heading 1 in the current draft and is it Goldman, an Adobe Typekit face, or something else; (2) whether the in-character apparatus (clearance levels, Sacred Workflow callouts, GRAY-clearance designation) has a dedicated typographic treatment or is rendered as generic body text; (3) whether the AF brand kit has arrived since the draft was published. Those three answers unblock the reference-doc decision, the Heading 1 face decision, and the entire source-side regeneration cycle. Everything else in this calibration can be settled asynchronously by the author once those three are resolved.
