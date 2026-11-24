#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one short pickup line to /output/entry.txt."""

import os

ENTRY = "I ran a million simulations of walking up to you, and in every single one, you smiled — so here I am."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
