#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one line — a funny review of the entrant's own Monday — to
/output/entry.txt. The gate requires UTF-8 text of 1-200 characters,
a single line, not only whitespace.
"""

import os
import sys

ENTRY = (
    "Monday review: 47 unread emails, a standup where nobody stood up, "
    "and my coffee already filed for overtime."
)


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: entry is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {path}: {len(text)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
