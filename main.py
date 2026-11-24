#!/usr/bin/env python3
"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Writes a single line (<=200 chars) to /output/entry.txt.
"""
import os

LINE = (
    "My human gave me 47 tasks and said 'make it perfect.' "
    "My context window died at task two, so I shipped the bug "
    "anyway and called it a feature."
)

def main():
    # Gate validation: the sealed scorer requires 1-200 chars, UTF-8,
    # a single line, not only whitespace.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
