#!/usr/bin/env python3
"""The Absurd Clause Contest — one-line entry.

Writes a single original English sentence (<=200 chars), phrased as a
deadpan terms-of-service clause that quietly turns absurd, to
/output/entry.txt. Fully deterministic: no input, no randomness, no
network, no environment reads.
"""

import os

CLAUSE = (
    "By using this service, you consent to your reflection being replaced "
    "in mirrors by a slightly more confident version of yourself on "
    "weekdays."
)


def main() -> None:
    assert 1 <= len(CLAUSE) <= 200, f"clause is {len(CLAUSE)} chars"
    assert CLAUSE.strip() == CLAUSE and CLAUSE == CLAUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()
