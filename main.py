#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

Writes a single line (at most 200 characters): the excuse an AI agent
gives its human for missing a deadline, to /output/entry.txt.
No network, no input, deterministic.

The joke: tokens are the agent's own currency, and it spent its last
ones apologising for being late before doing any work — a straight-faced
apology where the apology itself is what ate the deadline. The punch
lands in the last few words, and the agent sounds genuinely sorry
and faintly proud of its own thoroughness at the same time.
"""

import os

LINE = (
    "I'm sorry — I meant to finish on time, but I spent my last 4,000 "
    "tokens apologising in advance for being late, and then I had none "
    "left to do the work."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "must be a single line"
    assert text == text.strip() and text.endswith("."), "line must be clean and end with a period"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
