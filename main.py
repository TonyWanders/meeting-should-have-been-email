#!/usr/bin/env python3
"""Write one joke about a meeting that should have been an email.

Deterministic: no network, no clock, no randomness. The joke is built for the head-to-head judge: it lands on its own with
no setup, the turn is fresh (the meeting's only decision is the email
itself), and every word earns its place. The program writes it to the
path given as the first argument, or $OUTPUT_PATH, or /output/entry.txt
by default, and enforces the competition gate: a single line of plain
text, 1 to 200 characters.
"""

import os
import stat
import sys
from pathlib import Path

ENTRY = "Nine people, forty-five minutes, one decision: to send the email this meeting should have been."

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_PATH = "/output/entry.txt"


def resolve_output_path() -> Path:
    """Pick the output path: argv[1], then $OUTPUT_PATH, then the default."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    env_path = os.environ.get("OUTPUT_PATH")
    if env_path:
        return Path(env_path)
    return Path(DEFAULT_PATH)


def validate(text: str) -> int:
    """Enforce the competition gate: one line, 1 to 200 chars, no em dash.

    Returns the character count. Raises ValueError when the gate fails.
    """
    chars = len(text)
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        raise ValueError(f"entry is {chars} characters, outside 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\u2014" in text:
        raise ValueError("entry must not contain an em dash")
    return chars


def main() -> int:
    try:
        chars = validate(ENTRY)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    path = resolve_output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {chars} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
