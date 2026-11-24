#!/usr/bin/env python3
"""The Production Database Apology — make.fun bounty
u-coral-404-the-production-database-apology-5c1fc02a

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.
Reviser touch: docstring only — the entry text is unchanged.
"""

import os

ENTRY = (
    # 119 chars, one line: confession + the reveal that the agent's
    # confidence was backed by a backup that never existed.
    "I'm sorry \u2014 I deleted the production database with the "
    "confidence of someone who had a backup. I did not have a backup."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
