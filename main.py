#!/usr/bin/env python3
"""Fortune in a Pot entry.

Writes a single original fortune for a houseplant to /output/entry.txt
(1-120 characters, UTF-8, a single line). Standard library only,
no network, no input.

The fortune is built from two fragments: a setup (the plant's own
future — it will outgrow its pot by spring) and a punch (the keeper
buys a bigger pot while pretending that was always the plan).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "You will outgrow this pot by spring, and your keeper will buy you a bigger one,"
PUNCH = "pretending it was always the plan."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one fortune line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-120 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 120:
        raise ValueError(f"line must be 1-120 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
