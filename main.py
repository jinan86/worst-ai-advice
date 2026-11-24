#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open (make.fun).

Writes one line of deliberately terrible AI advice to /output/entry.txt.

The line: a backup tip that sounds helpful, tidy and confident, and is
exactly the sort of thing a reader could plausibly follow and then regret.
"""

import os
import sys

# One line, 140 characters max, no trailing newline games: the file holds
# exactly this text and nothing else.
ENTRY = (
    "For maximum efficiency, keep your only backup on the same disk "
    "as the original \u2014 everything stays neatly in one place."
)


def main() -> int:
    # Gate: UTF-8 text of 1 to 140 characters, not only whitespace.
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140) or not text.strip():
        print(f"entry is {len(text)} characters, outside the 1-140 gate",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic: identical bytes on every run.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
