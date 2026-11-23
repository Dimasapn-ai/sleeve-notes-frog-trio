#!/usr/bin/env python3
"""Sleeve Notes for the Frog Trio — make.fun entry.

Writes one text (album title + back-cover blurb) to entry.txt in the
output directory: $MAKEFUN_OUTPUT_DIR if set, else /output.
Standard library only; deterministic.
"""

import os

TITLE = "Lily Pad Sessions"

BLURB = (
    "The trio's fifth record, cut in one night at the Boathouse, where they "
    "hold the Friday residency. Alto sax close and dry, the bass walking "
    "the shallow end, brushes on a kit that has weathered nine summers. "
    "No guests, no gimmicks — three players listening hard, leaving "
    "space, and swinging."
)

# The gate counts title + blurb together: one newline between them,
# no trailing newline.
TEXT = TITLE + "\n" + BLURB


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
