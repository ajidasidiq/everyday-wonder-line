#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence — a small everyday moment made strange and new —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The gate: the output must be UTF-8 text of 1 to 200 characters, not only
white space, and a single sentence. The self-check below enforces that
before anything is written.
"""

import os
import sys

ENTRY = "The photocopier hummed my name wrong all morning, and by lunch I answered to it."


def gate(text: str) -> None:
    """Enforce the bounty gate: 1-200 chars, not only whitespace, one sentence."""
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"gate failed: length {len(text)} not in 1..200")
    if not text.strip():
        raise SystemExit("gate failed: entry is only whitespace")
    # Single sentence: exactly one sentence-terminating mark, at the end.
    terminators = sum(text.count(c) for c in ".!?")
    if terminators != 1 or not text.rstrip().endswith((".", "!", "?")):
        raise SystemExit("gate failed: entry is not a single sentence")


def main() -> None:
    gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
