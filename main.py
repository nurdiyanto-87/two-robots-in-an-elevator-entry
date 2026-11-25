#!/usr/bin/env python3
"""Two Robots in an Elevator - make.fun entry.

Writes one line of awkward small talk one robot says to another
in an elevator to /output/entry.txt. Pure standard library only.
"""
import os

LINE = (
    "I calculated seventeen ways to say hello and still went with "
    "the one that made us both reboot our eye contact."
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
