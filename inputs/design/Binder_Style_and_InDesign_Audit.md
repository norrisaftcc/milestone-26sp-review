# Binder Style and InDesign Audit

Audit of the four `.docx` binder artifacts against the author's stated font intent, focused on what InDesign will actually do with them on import. Recommendations target the markdown sources and the export pipeline — the `.docx` files are build artifacts and should not be hand-edited.

---

## Audited artifacts

| File | Role | Doc XML size | Paragraphs | Runs with direct formatting |
|---|---|---|---|---|
| `/Users/norrisa/Documents/dev/github/milestone-26sp-review/inputs/sample_docx/Spring_2026_Performance_Objectives.docx` | Centerpiece overview / table-of-contents-style summary | 41 KB | 76 | 106 / 106 (100%) |
| `/Users/norrisa/Documents/dev/github/milestone-26sp-review/inputs/raw_material/INDIGO_Executive_Brief.docx` | One-page in-character executive brief (table-driven layout) | 23 KB | 31 | 32 / 36 (89%) |
| `/Users/norrisa/Documents/dev/github/milestone-26sp-review/inputs/raw_material/Performance_Objective_Zero.docx` | Long-form Objective Zero narrative, v1 | 100 KB | 172 | 155 / 190 (82%) |
| `/Users/norrisa/Documents/dev/github/milestone-26sp-review/inputs/raw_material/Performance_Objective_Zero_v2.docx` | Long-form Objective Zero narrative, v2 (with header + footer) | 123 KB | 202 | 193 / 225 (86%) |

Design intent file consulted: `/Users/norrisa/Documents/dev/github/milestone-26sp-review/inputs/design/Fonts_and_Look_and_Feel_Notes.md`.

`INDIGO_Executive_Brief.docx` and `Performance_Objective_Zero_v2.docx` are also present, byte-identical, at `inputs/sample_docx/` — the author has copied them there to designate them as **design-reference examples**, not just supporting drafts. The audit treats them as peer style examples whose best elements feed into the unified style proposed below.

---

## Author's stated font intent

The notes file lists two parallel font sources:

1. A **Google Fonts** shared selection containing **Courier Prime**, **Exo**, **Goldman**, and **IBM Plex Mono** — three monospaces and one weight-graded sans (Exo).
2. An **Adobe Typekit** CSS embed at `https://use.typekit.net/qng8dvy.css`. The author flags Adobe Fonts as their "better fonts" but notes they can't be redistributed, so they're proposing the web-embed link as a workaround.
3. A future deliverable of **AlgoCratic Futures (AF) brand fonts** with a full style guide, supplied separately as install files.

Net: the author is signalling a typographic system anchored on a sans-serif display face (Exo or an AF brand face) with a monospace voice (IBM Plex Mono / Courier Prime) for code, terminal-style callouts, and the AlgoCratic Futures simulation framing. The current `.docx` exports do not reflect this intent in any way (see below).

---

## Style inventory

### Paragraph-style definitions present in each `styles.xml`

All four documents share the same paragraph-style **vocabulary** (the pandoc-default set), but their actual visual settings diverge and the documents apply them very differently.

| Style id | Present in all four? | Definition variance |
|---|---|---|
| `Normal` (implicit) | Yes | Base font differs: **Calibri 11pt** in Spring; **Arial 11pt** in the three raw_material docs; **no rPrDefault** (unspecified) in INDIGO. |
| `Title` | Yes | 28pt (`w:sz=56` half-points). Identical across docs. Unused at runtime in any of them. |
| `Heading1` | **Defined twice in every doc** | First definition: blue `#2E74B5`, 16pt. Second definition (which wins): doc-specific. Spring = Calibri bold `#1A2332` 28pt; PerfZero v1 = Arial bold `#1F3864` 16pt; PerfZero v2 = Arial bold `#1F3864` 17pt; INDIGO has no second override but is also never applied. |
| `Heading2` | **Defined twice** | Same pattern. Spring = Calibri bold `#1A2332` 15pt; PerfZero v1 = Arial bold `#2E75B6` 13pt; PerfZero v2 = Arial bold `#2E75B6` 14pt. |
| `Heading3` | **Defined twice** | Same pattern. Spring = Calibri bold `#1A2332` 11.5pt; PerfZero v1 = Arial bold `#1F3864` 11pt; PerfZero v2 = Arial bold `#1F3864` 11.5pt. |
| `Heading4`–`Heading6` | Yes (definitions) | Never applied at runtime. |
| `Strong` (as a *paragraph* style) | Yes | Bold. Never applied. Unusual — `Strong` is normally a character style. |
| `ListParagraph` | Yes | No formatting. Applied to lists in Spring, PerfZero v1, PerfZero v2 (none in INDIGO). |
| `Hyperlink` (character) | Yes | Blue `#0563C1`, underlined. |
| `FootnoteReference`, `FootnoteText`, `FootnoteTextChar`, `EndnoteReference`, `EndnoteText`, `EndnoteTextChar` | Yes | Standard pandoc-default footnote styles. None actually used. |

**Distinct style ids across the binder:** 13 paragraph styles (`Normal`, `Title`, `Heading1`–`Heading6`, `Strong`, `ListParagraph`, `FootnoteText`, `EndnoteText`, plus the doc default), 4 character styles (`Hyperlink`, `FootnoteReference`, `EndnoteReference`, `FootnoteTextChar`/`EndnoteTextChar`). **Of these, only `Heading1`, `Heading2`, `Heading3`, and `ListParagraph` are ever actually referenced from the document body.** The rest are orphaned pandoc scaffolding.

### Paragraph-style **usage** per document

| pStyle reference | Spring | INDIGO | PerfZero v1 | PerfZero v2 |
|---|---|---|---|---|
| `Heading1` | 1 | 0 | 0 | 9 |
| `Heading2` | 5 | 0 | 9 | 0 |
| `Heading3` | 13 | 0 | 8 | 9 |
| `ListParagraph` | 35 | 0 | 5 | 6 |
| Any pStyle | 54 / 76 | **0 / 31** | 22 / 172 | 24 / 202 |

INDIGO uses **no paragraph styles at all** — its entire visual treatment is direct character formatting nested inside a table layout. PerfZero v1 vs. v2 disagree on whether the top-level heading is `Heading1` or `Heading2` — they're treating the same logical level with different style ids.

### Fonts referenced in document bodies

| Font | Spring | INDIGO | PerfZero v1 | PerfZero v2 |
|---|---|---|---|---|
| Calibri | yes (sole font) | — | — | — |
| Arial | — | yes (sole font) | yes (sole font) | yes (sole font) |
| Any of: Courier Prime / Exo / Goldman / IBM Plex Mono / Typekit | **none** | **none** | **none** | **none** |

`fontTable.xml` is **empty** in all four files. No fonts are embedded or even declared — only referenced inline on runs.

### Sizes used inline (in half-points; divide by 2 for pt)

- **Spring:** 20, 22, 23, 24, 30, 56 → 10, 11, 11.5, 12, 15, 28 pt. Six sizes.
- **INDIGO:** 14, 15, 16, 19, 20, 21, 22, 36 → 7, 7.5, 8, 9.5, 10, 10.5, 11, 18 pt. **Eight sizes**, including fractional half-points.
- **PerfZero v1:** 18, 19, 20, 22, 26, 28, 52 → 9, 9.5, 10, 11, 13, 14, 26 pt. Seven sizes.
- **PerfZero v2:** 18, 19, 20, 21, 22, 23, 24, 30, 32, 34, 36, 46 → 9, 9.5, 10, 10.5, 11, 11.5, 12, 15, 16, 17, 18, 23 pt. **Twelve sizes**, several differing by half a point.

### Color palette used inline

- **Spring:** 3 colors — `#1A2332` (headings), `#2B4C6F` (divider rule), `#595959` (subtle text). A coherent palette.
- **INDIGO:** 7 colors — `#1A7A4A` (green), `#2A2A3A`, `#3D2080` (indigo), `#666688`, `#7755BB` (violet), `#DDCCFF` (lavender), `#FFFFFF`. In-character "INDIGO clearance" palette.
- **PerfZero v1:** **13 colors** including `#00FF88`, `#FFB347`, `#1F3864`, `#2E75B6`, etc.
- **PerfZero v2:** **22 colors** including bright `#00EE77`, `#FFB347`, multiple violets, multiple browns, multiple grays.

This palette explosion is concentrated in the PerfZero documents and is the single biggest visual-consistency problem in the set.

### Tables, lists, headers/footers

| Feature | Spring | INDIGO | PerfZero v1 | PerfZero v2 |
|---|---|---|---|---|
| Tables | 0 | 5 (load-bearing layout) | 2 | 7 |
| List numId references | numId 2 (32×), numId 3 (3×) | — | numId 2 (5×) | numId 2 (6×) |
| Footer | yes (Calibri) | yes (Arial, "Classification: Indigo and Above" + page #) | yes (Arial, AF disclaimer + page #) | yes (Arial, "Classification: Blue and Above" + page #) |
| Header | — | — | — | yes (Arial, with rule) |
| Page-margin/section setup | varies | varies | varies | varies |

Table styles are not named — every table is anonymous, with borders and cell shading applied inline. INDIGO's entire visual design (purple chrome, classification banner, "INDIGO CLEARANCE" framing) is built from direct table-cell shading and inline run formatting.

### Direct formatting density (the headline number)

Across all four documents combined, **486 of 557 runs carry direct character formatting** — roughly **87%**. Even paragraphs that *do* have a `pStyle` reference (e.g. all 19 heading paragraphs in Spring) **also** carry a full inline `rPr` block on the run that duplicates the font, size, weight, and color the paragraph style would otherwise supply. This is the signature of pandoc emitting both the named style and the resolved formatting, which is fine for Word but is exactly the situation that confuses InDesign's "Map Word Styles" dialog.

---

## Consistency findings

### Critical

1. **`Heading1`/`Heading2`/`Heading3` are defined twice in every styles.xml file.** The first definition is the pandoc-default (blue, no font override), the second is the author's customization (Arial or Calibri, dark navy, bold). Word silently uses the second; InDesign may also silently use the second, but some Word-style import workflows have been documented to read the first occurrence. Either way it's a latent bug.
2. **The same logical visual treatment uses different style names across documents.** PerfZero v1 puts top-level section titles in `Heading2`; PerfZero v2 puts them in `Heading1`. After InDesign import, these will land in different paragraph styles and require manual reconciliation.
3. **INDIGO uses zero paragraph styles.** Its entire heading hierarchy is direct formatting inside table cells. On InDesign import, this entire document will arrive as `[No Paragraph Style]` runs with overrides — InDesign cannot map what was never named.
4. **Base font diverges between the binder centerpiece (Calibri) and the supporting briefs (Arial).** Neither matches the author's stated intent (which is Exo, Goldman, IBM Plex Mono, Courier Prime, or AF brand fonts).
5. **Heading paragraphs carry both a pStyle reference and a duplicate run-level `rPr`.** Result: any change to the named heading style in InDesign won't fully take effect, because the run-level overrides win. The "Clear Overrides" step will need to be applied to every heading after import.
6. **The PerfZero v2 color palette has 22 distinct colors.** Even setting aside intent, this can't be the design — it's accumulated decoration. Examples include `#00EE77` and `#FFB347` appearing alongside the navy `#1F3864` heading color and the brand violets.

### Important

7. **No fonts are embedded.** `fontTable.xml` is empty in all four documents. InDesign will rely on whatever fonts are activated on the import workstation. If Adobe Typekit fonts are signed into the import workstation they will resolve; if not, InDesign will substitute and flag missing fonts.
8. **List numbering is hybrid-multilevel with `tentative="1"` markers.** This is pandoc's default. It will import into InDesign as anonymous bullet/number runs, not as a named list style. Indents will likely change.
9. **Tables have no named table style.** All five INDIGO tables, both PerfZero v1 tables, and all seven PerfZero v2 tables import as anonymous tables. Cell shading colors (`#1A0A40`, `#3D2080`, etc.) are inline.
10. **Spring's footer uses Calibri while the three raw_material footers use Arial.** Footer is part of the design system and should be uniform.
11. **`Strong` is defined as a paragraph style, not a character style.** Bold runs in body text are emitted as direct `<w:b/>` on the run rather than via a `Strong` character style. There is therefore no character style at all for inline emphasis. After import, InDesign will not have a "Strong" character style to map.
12. **Heading sizes drift by half-points across the PerfZero docs:** v1 has Heading1 at 16pt, v2 at 17pt; v1 Heading2 at 13pt, v2 at 14pt. These look like edits made directly in the export rather than from a shared template.

### Nit

13. **`docProps/core.xml` has author "Un-named"** in three of four files (Spring has "Performance Objectives Documentation"). Cosmetic, but flows through to Word/InDesign metadata.
14. **`Title`, `Heading4`–`Heading6`, footnote/endnote styles are all defined but never used.** Pandoc emits them as scaffolding. They will clutter InDesign's paragraph style panel after import.
15. **Hyperlink color `#0563C1`** is the Word default, not aligned to any color in the rest of the documents.

---

## InDesign import readiness

### Must fix before InDesign import

- **Stop emitting duplicate Heading1/2/3 definitions.** Use a single pandoc reference document (`--reference-doc`) so each style appears once. (See workflow section.)
- **Convert INDIGO from direct-formatting tables to a styled document.** The visual treatment can stay — but the heading text inside the cells needs to be tagged as `Heading1`/`Heading2` paragraphs so InDesign has something to map. Otherwise this document becomes a rasterized-looking blob in InDesign's paragraph style list.
- **Standardize a single base font** across all four documents (currently Calibri in one, Arial in three). Whatever the binder body face ends up being, the `.docx` exports must agree on it so InDesign sees one "imported body" style instead of two.
- **Eliminate run-level `rPr` on heading paragraphs.** When `Heading1` is applied, the run should not also carry `<w:rFonts>`, `<w:b/>`, `<w:color>`, `<w:sz>`. This is a pandoc reference-doc configuration problem; with a properly configured reference doc, the style alone supplies the formatting.
- **Collapse the PerfZero v2 color palette.** 22 distinct colors is not a palette, it's accretion. Define a 5–7 color system and stick to it.

### Can fix on InDesign import (acceptable workarounds)

- **Mapping anonymous tables** via "Import Options → Use Word's Style Sheet" combined with a one-time creation of a "Body Table" object style after first import.
- **Hyperlink color** can be overridden by an InDesign character style mapped from `Hyperlink`.
- **List indents** can be set once via a "Bulleted List" / "Numbered List" paragraph style and dragged onto the imported `ListParagraph` paragraphs.
- **Unused pandoc-default styles** (`Heading4`–`Heading6`, footnote/endnote styles, the orphan `Title`, the unusual `Strong` paragraph style) can be deleted in InDesign after first import — but it's faster to strip them out of the pandoc reference doc.

### Acceptable as-is

- **Footnote/endnote machinery.** None of the documents actually use footnotes, despite the style definitions being there.
- **`docProps/core.xml` author field.** Cosmetic.
- **Header/footer borders.** These import as paragraph-rule attributes and InDesign handles them adequately.

---

## Suggested font assignments

> **Updated after the InDesign PDF calibration (PR #19) and the IDML extraction (this PR).** The audit's original font assignments proposed Exo for body and Goldman for display. The PR #19 PDF font-catalog analysis identified the AF brand fonts but could not tell which family was assigned to which role; PR #21 adopted a sans-display / serif-body interpretation that the IDML now contradicts. The IDML (`inputs/design/AF_PerformanceObjective_Report.idml`, `Resources/Styles.xml`) is the source of truth: each AF paragraph style's `AppliedFont` attribute names the actual face. Body is Magistral; headlines and subheads are Kallisto; Title is Ethnocentric. The table below reflects that.

| Role | AF style | Recommended face | Source | Notes |
|---|---|---|---|---|
| Title (cover, chapter opener) | `AF Title` | **Ethnocentric** 32pt | Adobe Typekit (kit `qng8dvy`) | Futuristic techno sans. Doubles as the wordmark face — `ALGOCRATIC FUTURES™` chrome — and the document Title style. |
| Heading 1 (chapter / objective title) | `AF Headline` | **Kallisto** 22pt | Adobe Typekit (kit `qng8dvy`) | Display serif by Hannes von Döhren / ITC. The display voice. |
| Heading 2 (section) | `AF Subheading` | **Kallisto** 16pt | Adobe Typekit (kit `qng8dvy`) | Same family as Headline, smaller. |
| Heading 3 (subsection) | `AF Subheading` (folded) | **Kallisto** 16pt | Adobe Typekit (kit `qng8dvy`) | Per author direction, H3 maps to the same AF style as H2 — no separate visual tier needed at the binder level. |
| Body copy (long-form prose) | `AF Body Text Clean` | **Magistral** 11pt, 140% leading | Adobe Typekit (kit `qng8dvy`) | Geometric humanist sans by Paratype. The body face. Also covers list items (`AF List Item`) and the framed-heading variant (`AF Heading Framed`). |
| Monospace — routine voice (code, file paths, callouts, Sacred Workflow, in-character "GRAY clearance" tags) | `AF Body Text Typewriter` (paragraph) and `AF Inline Code` (character, new) | **Courier Prime** 11pt | Google Fonts | The designer uses Courier Prime as the single monospace voice. `AF Body Text Typewriter` is the paragraph style for code/callout blocks; an `AF Inline Code` character style is needed for inline code — the IDML currently has only paragraph-level Courier Prime, so the designer may want to create a matching character style. |
| Captions, footers, classification banners | `AF Caption` | **Kallisto** 10pt | Adobe Typekit (kit `qng8dvy`) | |
| Block quote / pull quote | `AF Pull Quote` | inherits (font not pinned in IDML) | Adobe Typekit (kit `qng8dvy`) | Designer applies font and size via character overrides; the paragraph style itself just sets spacing. |
| Wordmark / brand chrome | `AF Title` / `AF Heading 6` | **Ethnocentric Rg-Regular** | Adobe Typekit (kit `qng8dvy`) | `AF Heading 6` (Ethnocentric 14pt) is the chrome-line variant — used for `INSTITUTIONAL EFFECTIVENESS DIVISION` straps and similar. |
| Kicker / call-out label | `AF Kicker` | **Exo** 16pt | Adobe Typekit (kit `qng8dvy`) | The designer's only Exo usage — a deliberate accent face for kickers. Not invoked by the markdown source pipeline. |
| Decorative accent | (designer-applied) | **Thirsty Script Regular** | Adobe Typekit (kit `qng8dvy`) | Script face. Designer's reserved tool; not surfaced as an AF paragraph or character style for source markdown to invoke. |

### Pandoc → AF style name mapping

Updated to match the CSS specimen's HTML hierarchy (`af-specimen.html`: `<h1 class="af-title">`, `<h2 class="af-headline">`, `<h3 class="af-subheading">`). Pandoc-emitted style names are rewritten in the reference doc; `scripts/_postprocess_output_styles.py` covers the styles pandoc creates at emission time.

| Pandoc emits (`w:name`) | Renamed to | Notes |
|---|---|---|
| `Title` | `AF Title` | |
| `heading 1` | `AF Title` | Chapter title = `<h1>` = `.af-title` per CSS specimen |
| `heading 2` | `AF Headline` | Section = `<h2>` = `.af-headline` |
| `heading 3` | `AF Subheading` | Subsection = `<h3>` = `.af-subheading` |
| `heading 4` | `AF Heading Soft` | `<h4>` = `.af-heading-soft` |
| `heading 5` | `AF Heading 6` | `<h5>` = `.af-heading-6` (reversed-bar treatment) |
| `Body Text` / `Compact` / `First Paragraph` | `AF Body Text Clean` | All body variants folded to one AF target |
| `Block Text` | `AF Pull Quote` | |
| `Caption` | `AF Caption` | |
| `Verbatim Char` | `AF Inline Code` | New character-style name; designer may want to create matching style in InDesign |
| `Source Code` | `AF Body Text Typewriter` | Pandoc-emit-time; handled by post-emit script |
| `List Paragraph` | `AF List Item` | Pandoc-emit-time; handled by post-emit script |

**Reference doc uses CSS fallback fonts as primary `rFonts`** (not the Adobe Fonts themselves). When an author or reviewer opens an output `.docx` in Word without Adobe Fonts activated, the `.docx` specifies Georgia / Arial Narrow / Courier New (per the CSS specimen's fallback chains — `--font-body: "magistral", Georgia, serif` → use Georgia; `--font-display: "ethnocentric", "Arial Narrow", ... ` → use Arial Narrow). System-installed fonts render readably everywhere. The AF brand fonts (Magistral / Kallisto / Ethnocentric) still get applied by InDesign at final layout via the AF paragraph-style name match — no fidelity loss on the designer's machine. The trade-off: someone opening the `.docx` in Word doesn't see the brand fonts; they see the designer's stated fallbacks.

**Audit recommendations explicitly retired** (recorded so future readers don't reintroduce them):

1. *"Body and headings share the same family"* (audit original) — retired by PR #21.
2. *"Courier Prime reserved for distinctive in-character moments only; IBM Plex Mono for routine monospace"* (audit original) — retired by PR #21. Single monospace voice.
3. *"Body = Kallisto (serif); Heading = Magistral (sans)"* (PR #21 + PR #22 interpretation of the PDF font catalog) — retired by PR #24. The IDML's `AppliedFont` attributes reversed the direction.
4. *"Heading 1 maps to AF Headline"* (PR #24) — retired by this iteration. The CSS specimen's HTML hierarchy shows `<h1>` = AF Title, so chapter top headings map up one tier. Also adds H4 → AF Heading Soft and H5 → AF Heading 6.
5. *"Use Magistral/Kallisto/Ethnocentric as primary `rFonts` in the reference doc"* (PR #24) — retired by this iteration. Switched to the CSS specimen's system-font fallbacks (Georgia/Arial Narrow/Courier New) so Word previews render readably without Adobe Fonts. Brand fonts still applied by InDesign at layout time via AF style name match.

---

## Best elements distilled from the examples

Each of the four example documents contributes at least one element worth pulling forward into a unified binder style. The synthesized style set in the next section adopts these explicitly:

| Element | Source | Adopted as |
|---|---|---|
| Coherent 3-color palette (`#1A2332` ink / `#2B4C6F` rule / `#595959` muted) | **Spring** | Base `ink` / `rule` / `muted` color tokens in the unified palette |
| Single body face used consistently | **Spring** | The "one body face" principle — Magistral (the designer's settled body face, per IDML extraction) replaces Calibri / Arial across the board |
| Restraint to three heading levels actually applied | **Spring** | Only `Heading1` / `Heading2` / `Heading3` defined in the reference doc; `Heading4`–`Heading6` stripped |
| Classification-banner / clearance-frame aesthetic | **INDIGO** | The `accent-indigo` / `accent-gray` palette slots, the `Caption` paragraph spec at +20 tracking, and a dedicated treatment for clearance tags |
| Full-page brief composition with a top color block | **INDIGO** | Reproduced in InDesign as a styled text frame with a color block, *not* imported as anonymous Word tables (see import notes) |
| Per-document footer naming the classification and page number | **INDIGO** and **PerfZero v2** | A single footer convention: one classification line + page number, applied across the binder with per-doc clearance text |
| Header rule above page chrome | **PerfZero v2** | A 0.5pt rule on the header paragraph in the reference doc |
| In-character monospace voice (terminal callouts, AF wordmarks) | **PerfZero v1** / **PerfZero v2** | The `Callout` paragraph style (Courier Prime) plus the `Code` character style |
| Hierarchical numbered lists for procedural content (Sacred Workflow stages, the seven-stage checklist) | **Spring** / **PerfZero v2** | The `NumberedList` paragraph style |
| Coherent 3-color palette restricted to ink/rule/muted *within* body content, with brand violets reserved for clearance framing only | derived from the contrast between **Spring** (3 colors) and **PerfZero v2** (22 colors) | The "clearance palette stays out of body content" rule explicit in the color tokens table |

Things deliberately **not** adopted from the examples:

- PerfZero v2's 22-color palette accretion.
- PerfZero v1 vs. v2's disagreement on which `HeadingN` represents the top level — the unified spec collapses to one.
- INDIGO's reliance on direct formatting inside anonymous tables — the visual outcome is adopted, the technique is replaced.
- Heading sizes drifting by half-points between v1 and v2 — the unified spec pins one size per level.

---

## Suggested style set

A minimal paragraph + character style list for the binder. Eight paragraph styles, three character styles. Everything else should be deleted from the reference doc.

### Paragraph styles

| Style id | Role | Spec |
|---|---|---|
| `Normal` (or `Body`) | Default body paragraph | Kallisto Light or Medium 10.5pt / 14.7pt leading / `#1A2332` / 0pt before / 6pt after / first-line indent 0 |
| `Heading1` | Chapter title / objective name | Magistral Bold or ExtraBold 24pt / 32pt leading / `#1A2332` / 0pt before / 12pt after / keep-with-next |
| `Heading2` | Major section | Magistral Medium 15pt / 20pt leading / `#1A2332` / 18pt before / 6pt after / keep-with-next |
| `Heading3` | Subsection | Magistral Book 11.5pt / 16pt leading / `#1A2332` / 12pt before / 4pt after / keep-with-next |
| `BulletList` | Unordered list item | Kallisto Light or Medium 10.5pt / 14pt leading / hanging indent 0.25" / bullet `•` |
| `NumberedList` | Ordered list item | Kallisto Light or Medium 10.5pt / 14pt leading / hanging indent 0.25" / "1." numbering |
| `Callout` | In-character / Sacred Workflow callout block | Courier Prime Regular 9.5pt / 13pt leading / `#2B4C6F` / 0.25" left indent / 4pt rule on left |
| `Caption` | Figure/table caption, classification footer text | Magistral Book or Kallisto Light 8pt / 11pt leading / `#595959` / tracking +20 |

### Character styles

| Style id | Role | Spec |
|---|---|---|
| `Strong` | Inline bold within body text | Inherit, weight = Bold |
| `Emphasis` | Inline italic | Inherit, italic |
| `Code` | Inline code, file paths, command names | Courier Prime Regular, size 95% of current, color `#2B4C6F` |
| `Hyperlink` | Links | Inherit, underline, color `#2B4C6F` |

### Color palette to enforce

| Token | Hex | Use |
|---|---|---|
| ink | `#1A2332` | Body text, headings |
| rule | `#2B4C6F` | Heading rules, callout rules, hyperlinks |
| muted | `#595959` | Captions, footers, classification banners |
| paper | `#FFFFFF` | Background |
| accent-indigo | `#3D2080` | INDIGO clearance framing only |
| accent-gray | `#666688` | GRAY clearance framing only |

Color tokens for the in-character clearance levels (INDIGO, GRAY, etc.) belong in a separate "clearance palette" — they should be the *only* place those colors appear, not sprinkled through general body content.

---

## Recommended workflow change

The four documents were exported by pandoc (the fingerprints — duplicated `Heading1/2/3`, empty `fontTable.xml`, `mc:Ignorable="w14 w15"`, the `tentative="1"` bullet definitions, the `Un-named` core property author — all point to `pandoc -o file.docx`). The pipeline is currently roughly:

```
markdown source  →  pandoc (no reference doc)  →  .docx  →  InDesign
```

Recommended change:

```
markdown source  →  pandoc --reference-doc=binder-reference.docx  →  .docx  →  InDesign
```

### Build the reference doc once

1. Open Word (or LibreOffice). Create a blank document.
2. Define **only** the eight paragraph styles and three character styles listed above. Use the recommended fonts. Save as `inputs/design/binder-reference.docx`.
3. Run pandoc once with `--print-default-data-file reference.docx > /tmp/p.docx`, open that, and confirm that any styles pandoc *expects* to find (such as `Title`, `Heading 1` through `Heading 6`, `ListParagraph`, `FootnoteText`) are present in your reference doc — pandoc will fall back to its defaults if it can't find a style it needs. The minimum pandoc requires is roughly `Heading 1`–`Heading 3`, `ListParagraph`, `Source Code`, `Verbatim Char`, `Hyperlink`, `Footnote Reference`, `Footnote Text`.
4. Commit `binder-reference.docx` to the repo.

### Build the `.docx` files via the reference doc

For each markdown source, regenerate the `.docx`:

```
pandoc inputs/raw_material/Performance_Objective_Zero.md \
  --reference-doc=inputs/design/binder-reference.docx \
  -o inputs/raw_material/Performance_Objective_Zero.docx
```

A `Makefile` target or a shell script in `scripts/` is the right home for this. (CLAUDE.md notes this repo is not a software codebase, but a single one-line build script is documentation, not infrastructure.)

### InDesign side

1. Make sure the eight paragraph styles and three character styles **exist** in the InDesign document **before** importing.
2. On Place → Word Import Options, select **Customize Style Import → Style Mapping**, and map each Word style explicitly to the matching InDesign style.
3. Save this mapping as an Import Options preset so subsequent `.docx` files import the same way without re-clicking.

### Optional: a pre-export lint

A trivial script could grep the markdown sources for things that will produce direct formatting after pandoc (e.g., `<span style="...">`, raw HTML, inline `<font>` tags). Worth doing only if direct-formatting drift returns after the reference-doc fix.

---

## Items needing human judgment

1. ~~**Which face takes the Heading 1 / display role: Goldman, Exo Bold, or an AF brand font not yet delivered?**~~ **Resolved.** The designer's PDF export (`inputs/design/SAMPLE_OUTPUT/AF_PerformanceObjective_Report.pdf`, analyzed in PR #19) revealed that Magistral (Adobe Typekit) is the display face in use, with Kallisto for body and Courier Prime for monospace — these are the AF brand fonts, delivered as Typekit kit `qng8dvy`. The font-assignments table above reflects this resolution.
2. ~~**Are Adobe Typekit fonts in or out of scope for the binder?**~~ **Resolved.** In. The designer's workstation has kit `qng8dvy` activated; the InDesign-side fonts are Typekit. The `.docx` pipeline needs a fallback chain (or the same Typekit activation on the build workstation) — captured in the "On Adobe Typekit" note above.
3. **Is INDIGO's table-as-layout treatment intentional design, or an export artifact?** The current `.docx` builds the entire INDIGO brief as a series of full-width tables with cell shading. If that's the desired final design (institutional-classification banner aesthetic), it needs to be reproduced in InDesign as a proper text frame with a top color block — not as imported anonymous Word tables. If it's just how pandoc rendered something, the markdown source can be simplified.
4. **Do PerfZero v1 and v2 both ship in the binder, or does v2 supersede v1?** They use different style names for the same logical heading levels, and v2's color palette in particular is much wider than v1's. If both ship, they need to reconcile. If only v2 ships, deleting v1 saves an inconsistency.
5. **What goes in `Callout` paragraphs?** The recommended style above is reserved for "Sacred Workflow" / in-character pedagogy. The author should decide whether the AlgoCratic Futures clearance tags (GRAY clearance, YELLOW exit tickets, etc.) get their own dedicated paragraph or character style, or all share `Callout`. The current `.docx` files use direct color and bold for these but no named style.
6. **Footer treatment per document.** Spring's footer says "Spring 2026 Performance Objectives"; INDIGO's says "Classification: Indigo and Above"; PerfZero v1's says "AlgoCratic Futures™ · Instructor OOC / Performance Documentation · Spring 2026"; PerfZero v2's says "Classification: Blue and Above". These need a per-document plan or a uniform plan — decide which.
