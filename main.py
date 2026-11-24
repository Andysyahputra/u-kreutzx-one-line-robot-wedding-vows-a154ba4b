#!/usr/bin/env python3
"""One-line robot wedding vows entry.

Builds the vow from its three beats — the promise, the robot
condition, and the closing twist — then writes exactly that one
line (plus a trailing newline) to /output/entry.txt.

Deterministic: no input, no randomness, no network, no time.
"""

from pathlib import Path

# The three beats of the vow, joined with spaces.
OPENING = "I take you as my partner,"
CONDITION = "in sickness and in low battery,"
CLOSING = "until a factory reset do us part."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 160


def build_vow() -> str:
    """Assemble the single-line vow from its beats."""
    parts = [OPENING, CONDITION, CLOSING]
    return " ".join(parts)


def validate(line: str) -> None:
    """Guard the competition gate: one line, 1-160 chars, no newlines."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry length {len(line)} outside 1-{MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def write_entry(line: str, path: Path = OUTPUT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    line = build_vow()
    validate(line)
    write_entry(line)


if __name__ == "__main__":
    main()
