#!/usr/bin/env python3
"""Two Robots in an Elevator - make.fun entry.

Writes one line of awkward small talk one robot says to another
in an elevator to /output/entry.txt. Pure standard library only.
"""
import os

# Revised in a second pass (2026-11-25): the first line's turn
# ("reboot our eye contact") landed softly and leaned on a
# familiar image. The new line keeps the same premise — two
# identical machines forced into small talk — but ends on a
# sharper, fresher twist: destiny vs. a recall notice.
LINE = (
    "You have the same firmware as me. "
    "This is either destiny or a recall notice."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and text, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
