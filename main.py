#!/usr/bin/env python3
"""One Letter for Your Day — entry generator.

Writes exactly one character, the letter Z, to entry.txt.
Behind Z sits the word for the day: zero sleep — the night ran out
before the body did, and the day was lived on fumes.
"""

import os

LETTER = "Z"


def main() -> None:
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be one A-Z letter"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and verify the gate: exactly 1 byte, one A-Z letter, no newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert len(raw) == 1 and b"A" <= raw <= b"Z", "entry.txt must be exactly one A-Z byte"


if __name__ == "__main__":
    main()
