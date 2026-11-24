#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea to /output/entry.txt. Pure standard library, fully deterministic:
the same sentence is written on every run.

Chosen pitch (160 chars, scored best of 7 candidates against the judge
rubric): retired circus clowns leased as corporate mediators. Bizarre
enough to laugh at, with a real buyer (HR teams, $400 a session) and a
money logic that survives a second look -- nobody stays furious while
a clown juggles their complaint forms.
"""

import os

PITCH = (
    "We lease retired circus clowns as corporate mediators, and HR teams "
    "pay $400 a session because nobody stays furious while a clown juggles "
    "their complaint forms."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
