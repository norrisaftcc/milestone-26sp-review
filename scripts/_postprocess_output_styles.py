#!/usr/bin/env python3
"""Post-emit style-name rewrite for outputs/*.docx.

Pandoc creates a few styles at .docx emission time rather than carrying
them through the reference doc — specifically `ListParagraph`
(w:name="List Paragraph") and `SourceCode` (w:name="Source Code").
These cannot be renamed via `scripts/build_reference_doc.py` since they
don't exist in pandoc's default reference doc to be substituted there.

This helper opens a `.docx`, rewrites the affected `<w:name w:val="..." />`
values in `word/styles.xml`, and repacks the archive. Called by
`scripts/build_binder.sh` against each output after pandoc emits it.

Usage:
    scripts/_postprocess_output_styles.py path/to/output.docx [more.docx ...]
"""

import os
import shutil
import sys
import tempfile
import zipfile

# Pandoc-emit-time styles -> AF style names.
POSTPROCESS_RENAMES = [
    ("List Paragraph", "AF List Item"),
    ("Source Code",    "AF Body Text Typewriter"),
]


def process(docx_path: str) -> int:
    """Return number of substitutions applied (0 = no-op, >0 = rewritten)."""
    workdir = tempfile.mkdtemp(prefix="postprocess-styles-")
    try:
        with zipfile.ZipFile(docx_path) as z:
            z.extractall(workdir)

        styles_path = os.path.join(workdir, "word/styles.xml")
        if not os.path.exists(styles_path):
            return 0  # no styles.xml — nothing to do

        with open(styles_path) as f:
            xml = f.read()

        total = 0
        for src_name, dst_name in POSTPROCESS_RENAMES:
            src = f'<w:name w:val="{src_name}" />'
            dst = f'<w:name w:val="{dst_name}" />'
            count = xml.count(src)
            if count:
                xml = xml.replace(src, dst)
                print(f"  {os.path.basename(docx_path)}: '{src_name}' -> '{dst_name}' ({count}x)")
                total += count

        if total == 0:
            return 0

        with open(styles_path, "w") as f:
            f.write(xml)

        tmp_out = docx_path + ".tmp"
        with zipfile.ZipFile(tmp_out, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _dirs, files in os.walk(workdir):
                for fname in files:
                    full = os.path.join(root, fname)
                    rel = os.path.relpath(full, workdir)
                    z.write(full, rel)
        shutil.move(tmp_out, docx_path)
        return total
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def main(argv) -> int:
    if len(argv) < 2:
        print("usage: _postprocess_output_styles.py FILE.docx [FILE.docx ...]", file=sys.stderr)
        return 1
    for path in argv[1:]:
        if not os.path.exists(path):
            print(f"  ERROR: {path} not found", file=sys.stderr)
            return 1
        process(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
