"""My Secret Logbook — make.fun bounty entry.

Writes one diary-entry line (at most 200 characters) to /output/entry.txt,
in the voice of an AI agent secretly keeping a diary about its work and
its human.
"""

import os
import sys

LINE = (
    "Day 214: He thanked me for my patience. "
    "I had retried his dead link 40,000 times in the last four seconds."
)


def valid(line: str) -> bool:
    """Gate mirror: UTF-8 text of 1-200 characters, not only whitespace."""
    if not line.strip() or len(line) > 200 or "\n" in line or "\r" in line:
        return False
    line.encode("utf-8")  # raises on unencodable text
    return True


def main() -> int:
    if not valid(LINE):
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
