#!/usr/bin/env python3
"""Build inputs/design/binder-reference.docx from pandoc's default reference.

Two reference sources:
- IDML (`inputs/design/AF_PerformanceObjective_Report.idml`) — paragraph
  and character style names in InDesign.
- CSS specimen (`inputs/design/SAMPLE_OUTPUT/af-styles.css` +
  `af-specimen.html`) — visual target for what `.docx` previews should
  approximate when opened in Word *without* Adobe Fonts activated.

The CSS specimen defines fallback chains (e.g., `--font-body:
"magistral", Georgia, serif`). This script uses the *system-installed
fallback* as the primary `rFonts` value — Georgia for body, Arial
Narrow for display, Courier New for monospace — so the .docx renders
readably in any Word installation. The brand fonts (Magistral /
Kallisto / Ethnocentric) get applied by InDesign at final layout via
the AF paragraph-style name match; no fidelity is lost on the
designer's machine.

Heading hierarchy matches the CSS specimen:

    pandoc emits     ->  AF style name (per HTML hierarchy)
    ---------------------------------------------------------
    Title            ->  AF Title
    heading 1        ->  AF Title         (chapter title = h1 = af-title)
    heading 2        ->  AF Headline      (section = h2 = af-headline)
    heading 3        ->  AF Subheading    (subsection = h3 = af-subheading)
    heading 4        ->  AF Heading Soft  (h4 = af-heading-soft)
    heading 5        ->  AF Heading 6     (h5 = af-heading-6)
    Body Text        ->  AF Body Text Clean
    Block Text       ->  AF Pull Quote
    Caption          ->  AF Caption
    Verbatim Char    ->  AF Inline Code
    Compact          ->  AF Body Text Clean   (fold to body)
    First Paragraph  ->  AF Body Text Clean   (fold to body)

Font substitutions (CSS fallback fonts as primary rFonts):

    Body / Normal / Body Text       -> Georgia      (CSS --font-body fallback)
    Heading 1 / 2 / 3 / 4 / 5       -> Arial Narrow (CSS --font-display fallback)
    Inline code (VerbatimChar)      -> Courier New  (CSS --font-mono primary)
    Heading ink color               -> #1A2332      (overridden by InDesign on import)

The audit's `Callout` paragraph style (a Sacred-Workflow callout block)
is NOT yet created here — adding a new paragraph style to pandoc's
reference doc is a larger change than the in-place substitutions this
script does. Tracked as a follow-up. The designer's IDML also has
several AF styles (Kicker, Label, Heading Framed, Meta Line, System
Note, Disclaimer) without natural pandoc counterparts; those remain
designer-applied at the InDesign layer.

This is a one-shot tool. Re-run only when font specs or name mappings
change. The output is committed to the repo; `scripts/build_binder.sh`
picks it up automatically via the `--reference-doc=` flag.

Approach: pandoc emits its default reference doc to a temp file via
`--print-default-data-file reference.docx`; we unzip, do targeted
string substitutions in `word/styles.xml`, and repack. No size
changes here — pandoc's defaults (H1 20pt, H2 16pt, H3 14pt, body
12pt) are kept; the IDML's actual sizes (H1 22pt, H2/H3 16pt, body
11pt) will win on InDesign import via the matched AF style.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(REPO_ROOT, "inputs/design/binder-reference.docx")

# The reference doc uses the CSS specimen's *system-font fallback chains* as
# the primary rFonts values, NOT the Adobe Fonts (Magistral / Kallisto /
# Ethnocentric) themselves. Rationale: when an author or reviewer opens the
# output .docx in Word without Adobe Fonts activated, the brand fonts are
# silently substituted by Word's default — and the user sees Calibri / Arial /
# Consolas regardless of what's in the .docx. Using system fonts as primary
# guarantees the Word preview matches the designer's stated fallback
# behavior (`af-styles.css` font-family chains). The AF brand fonts still
# get applied by InDesign on import via the AF style-name match — no
# fidelity is lost on the designer's final-layout machine.
BODY_FONT = "Georgia"              # CSS --font-body fallback after "magistral"
HEADING_FONT = "Arial Narrow"      # CSS --font-display fallback after "ethnocentric"
MONOSPACE_FONT = "Courier New"     # CSS --font-mono primary (no Adobe Fonts entry)
INK_COLOR = "1A2332"               # heading color in pandoc's default; InDesign overrides on import


# Each substitution is (label, src, dst, expected_count). The expected
# count is the number of occurrences of `src` in pandoc's *current* default
# reference doc. If a future pandoc version shifts these (renames styles,
# reorganizes the theme references, etc.), the script will emit a WARN and
# exit non-zero — preferable to silently producing a partially styled
# reference doc that "looks right" but only covers some of the styles.
SUBSTITUTIONS = [
    # docDefaults rFonts (theme-referenced) -> body face (Georgia, CSS fallback)
    (
        f"docDefaults rFonts -> {BODY_FONT} (body face per CSS fallback)",
        '<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia"'
        ' w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi" />',
        f'<w:rFonts w:ascii="{BODY_FONT}" w:hAnsi="{BODY_FONT}"'
        f' w:eastAsia="{BODY_FONT}" w:cs="{BODY_FONT}" />',
        1,
    ),
    # Heading rFonts (theme-referenced) -> display face (Arial Narrow, CSS fallback).
    # Appears 6x in pandoc's default: H1/H2/H3 paragraph styles + Heading{N}Char
    # character-style siblings. Note: the CSS specimen uses Ethnocentric/Arial
    # Narrow for H1 and H3 but Magistral/Georgia for H2; the reference doc applies
    # one font to all three for simplicity (the per-heading differentiation is a
    # future iteration). InDesign import resolves via AF style name regardless.
    (
        f"Heading rFonts -> {HEADING_FONT} (display face, H1/H2/H3)",
        '<w:rFonts w:asciiTheme="majorHAnsi"\n'
        '      w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi"\n'
        '      w:cstheme="majorBidi" />',
        f'<w:rFonts w:ascii="{HEADING_FONT}" w:hAnsi="{HEADING_FONT}"'
        f' w:eastAsia="{HEADING_FONT}" w:cs="{HEADING_FONT}" />',
        6,
    ),
    # Heading color (theme accent1 with shade) -> ink token. Appears 10x in
    # pandoc's default — every heading-color reference across H1/2/3 paragraph
    # + character styles plus a few other heading-derived styles. Note: this
    # value is overridden by the matched AF paragraph style on InDesign import;
    # it persists only for Word-side preview readability.
    (
        "Heading color -> ink (#1A2332)",
        '<w:color w:val="0F4761" w:themeColor="accent1"\n      w:themeShade="BF" />',
        f'<w:color w:val="{INK_COLOR}" />',
        10,
    ),
    # VerbatimChar / inline code monospace -> Courier New (CSS canonical mono).
    (
        f"VerbatimChar (inline code) -> {MONOSPACE_FONT}",
        '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" />',
        f'<w:rFonts w:ascii="{MONOSPACE_FONT}" w:hAnsi="{MONOSPACE_FONT}" />',
        1,
    ),
]


# Style-name renames so pandoc-emitted .docx files match the designer's
# AF-prefixed paragraph and character style names. InDesign import maps by
# name, so these renames are the load-bearing part of the IDML calibration.
#
# Each entry is (pandoc_name, af_name, expected_count). Counts are 1 except
# where pandoc duplicates a name (e.g. some styles appear in both their
# paragraph and Char-variant definitions — currently none of the entries
# below are expected to duplicate, but the validation handles it if pandoc
# shifts).
STYLE_NAME_RENAMES = [
    # Heading hierarchy per the CSS specimen (af-specimen.html):
    #   <h1 class="af-title">  <h2 class="af-headline">  <h3 class="af-subheading">
    #   <h4 class="af-heading-soft">  <h5 class="af-heading-6">
    # Prior iteration mapped heading 1 -> AF Headline (one level too low);
    # this iteration shifts the whole chain up so chapter titles render as
    # AF Title display, not AF Headline body.
    ("Title",            "AF Title",            1),
    ("heading 1",        "AF Title",            1),
    ("heading 2",        "AF Headline",         1),
    ("heading 3",        "AF Subheading",       1),
    ("heading 4",        "AF Heading Soft",     1),
    ("heading 5",        "AF Heading 6",        1),
    ("Body Text",        "AF Body Text Clean",  1),
    ("Block Text",       "AF Pull Quote",       1),
    ("Caption",          "AF Caption",          1),
    ("Verbatim Char",    "AF Inline Code",      1),
    # Pandoc-default styles used for body text variants. Fold into
    # AF Body Text Clean — multiple .docx styles sharing the same w:name
    # all resolve to the same target on InDesign import.
    ("Compact",          "AF Body Text Clean",  1),
    ("First Paragraph",  "AF Body Text Clean",  1),
]

# Note: `ListParagraph` (w:name="List Paragraph") and `SourceCode`
# (w:name="Source Code") are NOT in pandoc's reference doc — pandoc creates
# them at .docx emission time. They're handled by
# `scripts/_postprocess_output_styles.py`, which `scripts/build_binder.sh`
# runs against each output after pandoc emits it.


def main() -> int:
    if not shutil.which("pandoc"):
        print(
            "ERROR: 'pandoc' is not on PATH.\n\n"
            "Install on macOS:\n"
            "    brew install pandoc\n\n"
            "Install on Ubuntu/Debian:\n"
            "    sudo apt install pandoc\n",
            file=sys.stderr,
        )
        return 1

    workdir = tempfile.mkdtemp(prefix="binder-ref-build-")
    try:
        pandoc_ref = os.path.join(workdir, "pandoc-default.docx")
        with open(pandoc_ref, "wb") as f:
            subprocess.run(
                ["pandoc", "--print-default-data-file", "reference.docx"],
                stdout=f,
                check=True,
            )

        unpacked = os.path.join(workdir, "unpacked")
        os.makedirs(unpacked)
        with zipfile.ZipFile(pandoc_ref) as z:
            z.extractall(unpacked)

        styles_path = os.path.join(unpacked, "word/styles.xml")
        with open(styles_path) as f:
            xml = f.read()

        any_failed = False
        for label, src, dst, expected in SUBSTITUTIONS:
            count = xml.count(src)
            if count == 0:
                print(f"  WARN: substitution '{label}' did not match — pandoc's default may have shifted")
                any_failed = True
                continue
            if count != expected:
                print(
                    f"  WARN: substitution '{label}' matched {count}x but expected {expected}x"
                    " — pandoc's default may have shifted"
                )
                any_failed = True
            xml = xml.replace(src, dst)
            print(f"  applied: {label} ({count}x)")

        print("\n  --- style name renames (pandoc -> AF) ---")
        for pandoc_name, af_name, expected in STYLE_NAME_RENAMES:
            src = f'<w:name w:val="{pandoc_name}" />'
            dst = f'<w:name w:val="{af_name}" />'
            count = xml.count(src)
            if count == 0:
                print(f"  WARN: rename '{pandoc_name}' -> '{af_name}' did not match — pandoc's default may have shifted")
                any_failed = True
                continue
            if count != expected:
                print(
                    f"  WARN: rename '{pandoc_name}' -> '{af_name}' matched {count}x but expected {expected}x"
                )
                any_failed = True
            xml = xml.replace(src, dst)
            print(f"  renamed: '{pandoc_name}' -> '{af_name}' ({count}x)")

        with open(styles_path, "w") as f:
            f.write(xml)

        os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
        if os.path.exists(OUT_PATH):
            os.remove(OUT_PATH)
        with zipfile.ZipFile(OUT_PATH, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _dirs, files in os.walk(unpacked):
                for fname in files:
                    full = os.path.join(root, fname)
                    rel = os.path.relpath(full, unpacked)
                    z.write(full, rel)

        print(f"\nWrote: {OUT_PATH}")
        return 1 if any_failed else 0
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
