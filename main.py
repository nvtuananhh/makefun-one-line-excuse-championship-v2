#!/usr/bin/env python3
"""One-line excuse entry for The One-Line Excuse Championship.

Writes the single entry line to /output/entry.txt.
Stdlib only; deterministic: the same fixed string on every run.
"""

import os
from pathlib import Path

ENTRY = "I didn't ignore your 43 unread messages — I read all 43 and decided silence was the most helpful reply."


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
