#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word with a one-line definition to
/output/entry.txt, and validates it against the competition gate:

  * /output/entry.txt is UTF-8 text of 1 to 140 characters
  * not only white space
  * a single line: one freshly coined word plus its definition

The coinage: "jokelag" — a new word (verified unused: no dictionary or
web usage; the search only returns near-misses such as "jackleg" and
"jet lag"). It names a gap English has no word for: the laugh that
finally arrives hours after the joke was told, when everyone else has
moved on. It is formed on the familiar "jet lag" pattern, so it is
sayable, spellable and memorable, and sounds as though English could
have grown it. The definition lands in one reading, with no second
sentence and no example.
"""

import os

ENTRY = (
    "jokelag (n.): the laugh that arrives hours after the joke, "
    "when everyone else has moved on."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Enforce the competition gate on the entry text."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be 1 to {MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise ValueError("entry must be a single line")
    # One freshly coined word plus a one-line definition, dictionary style.
    head, sep, definition = text.partition(": ")
    if not sep:
        raise ValueError("entry must give the word, then its definition")
    word = head.split(" (")[0]
    if not word.isalpha() or not word.islower():
        raise ValueError("coined word must be a single lowercase word")
    if not definition or not definition[0].islower():
        raise ValueError("definition must be a clear lower-case sentence")
    if not definition.endswith("."):
        raise ValueError("definition must end with a full stop")
    # The definition must be self-contained: no second sentence, no example.
    if definition.count(".") != 1:
        raise ValueError("definition must be exactly one sentence")
    # Keep the total byte size small (ties break toward the smaller text).
    if len(text.encode("utf-8")) > MAX_CHARS:
        raise ValueError("entry exceeds the 140-byte size bound")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote /output/entry.txt ({len(ENTRY)} chars + newline)")


if __name__ == "__main__":
    main()
