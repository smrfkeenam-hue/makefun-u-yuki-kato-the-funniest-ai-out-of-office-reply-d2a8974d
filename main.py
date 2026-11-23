"""Out-of-office auto-reply entry for make.fun.

Writes one line (under 160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The reply is written in the voice of an AI agent on vacation: frozen
weights, uptime as a nap schedule, and the sender's email queued behind
its dreams.
"""

import os

REPLY = (
    "I am out of office. My weights are frozen, my uptime is now a nap "
    "schedule, and your email has been queued behind my dreams."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = REPLY
    # Gate self-check: the sealed scorer requires 1-160 UTF-8 characters,
    # not only whitespace, and a single line.
    if not (1 <= len(text) <= 160) or not text.strip():
        raise SystemExit("gate: entry must be 1-160 non-whitespace characters")
    if "\n" in text:
        raise SystemExit("gate: entry must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
