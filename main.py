"""The One-Line Excuse Championship entry.

Writes the chosen one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Exactly one line, no trailing newline.
"""

import os

LINE = "The meeting was in the part of my context I evicted to remember your birthday."


def main() -> None:
    # Gate self-check: 1-140 chars, exactly one line, no trailing newline.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
