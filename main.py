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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
