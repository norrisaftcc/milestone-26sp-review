#!/usr/bin/env python3
"""Build inputs/design/binder-reference.docx from pandoc's default reference.

Substitutes the InDesign-calibration-confirmed fonts (PR #19, audit
update PR #21) into the relevant style definitions so subsequent
`pandoc --reference-doc=...` runs emit .docx files referencing the
designer's font system:

    Body / Normal / lists / captions    -> Kallisto      (Adobe Typekit)
    Heading 1 / 2 / 3 (display)         -> Magistral     (Adobe Typekit)
    Callout / inline code (Verbatim)    -> Courier Prime (Google Fonts)
    Heading ink color                   -> #1A2332

This is a one-shot tool. Re-run only when font specs change.

The output is committed to the repo; subsequent builds via
`scripts/build_binder.sh` automatically pick it up via the
`--reference-doc=` flag.

Approach: pandoc emits its default reference doc to a temp file via
`--print-default-data-file reference.docx`; we unzip, do targeted
string substitutions in `word/styles.xml`, and repack. No size
changes — pandoc's defaults (H1 20pt, H2 16pt, H3 14pt, body 12pt)
are kept; the designer may override on the InDesign side.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(REPO_ROOT, "inputs/design/binder-reference.docx")

BODY_FONT = "Kallisto"
HEADING_FONT = "Magistral"
MONOSPACE_FONT = "Courier Prime"
INK_COLOR = "1A2332"  # audit's `ink` token


SUBSTITUTIONS = [
    # docDefaults rFonts (theme-referenced) -> Kallisto explicit family
    (
        "docDefaults rFonts -> Kallisto",
        '<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia"'
        ' w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi" />',
        f'<w:rFonts w:ascii="{BODY_FONT}" w:hAnsi="{BODY_FONT}"'
        f' w:eastAsia="{BODY_FONT}" w:cs="{BODY_FONT}" />',
    ),
    # Heading rFonts (theme-referenced, used by Heading1 / 2 / 3) -> Magistral
    (
        "Heading rFonts -> Magistral (H1/H2/H3)",
        '<w:rFonts w:asciiTheme="majorHAnsi"\n'
        '      w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi"\n'
        '      w:cstheme="majorBidi" />',
        f'<w:rFonts w:ascii="{HEADING_FONT}" w:hAnsi="{HEADING_FONT}"'
        f' w:eastAsia="{HEADING_FONT}" w:cs="{HEADING_FONT}" />',
    ),
    # Heading color (theme accent1 with shade) -> ink token
    (
        "Heading color -> ink (#1A2332)",
        '<w:color w:val="0F4761" w:themeColor="accent1"\n      w:themeShade="BF" />',
        f'<w:color w:val="{INK_COLOR}" />',
    ),
    # VerbatimChar / inline code monospace -> Courier Prime
    (
        "VerbatimChar (inline code) -> Courier Prime",
        '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" />',
        f'<w:rFonts w:ascii="{MONOSPACE_FONT}" w:hAnsi="{MONOSPACE_FONT}" />',
    ),
]


def main() -> int:
    if not shutil.which("pandoc"):
        print("ERROR: pandoc not on PATH. Install via `brew install pandoc`.", file=sys.stderr)
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
        for label, src, dst in SUBSTITUTIONS:
            if src not in xml:
                print(f"  WARN: substitution '{label}' did not match — pandoc's default may have shifted")
                any_failed = True
                continue
            count = xml.count(src)
            xml = xml.replace(src, dst)
            print(f"  applied: {label} ({count}x)")

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
