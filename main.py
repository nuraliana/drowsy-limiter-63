"""Write the bounty entry to the output directory.

The program is deliberately small: it holds one fixed entry text,
checks it against the bounty gate (plain UTF-8 text, 1 to 400
characters, one or two sentences, not only whitespace), and writes
it with no trailing newline to ``entry.txt`` inside the directory
named by MAKEFUN_OUTPUT_DIR, or /output when that is unset.

Standard library only. No network, no randomness, no timestamps,
no reading of other files. The script finds its output directory
from the environment, never from the working directory.
"""

import os
import sys

ENTRY = (
    "I asked the agent to add rate limiting. It rate-limited the health check, "
    "so the load balancer decided the service was dead and killed every instance, one by one, on schedule."
)


def sentence_count(text):
    """Count sentences by their closing punctuation."""
    return sum(1 for ch in text if ch in ".!?")


def main():
    entry = ENTRY
    if not entry or not entry.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if not 1 <= len(entry) <= 400:
        print(f"error: entry is {len(entry)} characters, must be 1-400",
              file=sys.stderr)
        return 1
    sentences = sentence_count(entry)
    if not 1 <= sentences <= 2:
        print(f"error: entry has {sentences} sentences, must be 1-2",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    print(f"wrote {len(entry)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
