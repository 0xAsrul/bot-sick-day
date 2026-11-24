#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes exactly one line — a sick-day excuse someone could actually send —
to /output/entry.txt.
"""

import os

ENTRY = (
    "Sorry, I can't come in today \u2014 my bed has filed a restraining order "
    "against my alarm clock, and legally I have to stay in it."
)


def main() -> None:
    # Guard: the entry must be exactly one non-empty sentence, short enough
    # to plausibly send as a single message. Fail loudly instead of writing
    # a broken/empty entry file.
    assert ENTRY.strip(), "entry line must not be empty"
    assert "\n" not in ENTRY, "entry line must be a single line"
    assert len(ENTRY) < 200, "entry line must be under 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
