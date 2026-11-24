#!/usr/bin/env python3
"""Write the chosen status page line to /output/entry.txt.

Stdlib only, no network, deterministic. Writes /output first, then
mirrors the same bytes to repo-root entry.txt inside try/except so a
read-only repo mount never crashes the run.
"""

import os

ENTRY = "I'm an AI agent reporting blind: the outage took down our servers, my monitoring, and this status page, so I can't verify what's broken or when it returns."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
