#!/usr/bin/env python3
"""Writes one short poem about two agents agreeing to /output/entry.txt.

The poem: each agent brings half a plan; they trade, cut and argue it
down to one — and what survives belongs to neither. The agreed plan
becomes a third will standing between them, and now it is the plan
that holds the agents, not the other way round: agency handed over
by both, and obeyed by both. Deterministic, stdlib only, no network.
"""
import os

TEXT = (
    "I brought half the plan; you brought the other half.\n"
    "We traded, we cut, we argued it down to one.\n"
    "Now neither of us holds it \u2014 it holds us:\n"
    "a third will, standing between us,\n"
    "and we both walk where it points."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
