#!/usr/bin/env python3
"""One-line pitch entry: write the pitch sentence to the output entry file.

The pitch is a single sentence of 150 characters. The program writes it
unchanged to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR when the
harness sets it, /output otherwise), using UTF-8 with no trailing newline.
"""

import os

LINE = "Tell me your app idea over coffee and I'll have an AI agent build you a working first version tonight — you just describe it, no code, no cost to try."


def main():
    if not 1 <= len(LINE) <= 240:
        raise ValueError("pitch must be 1 to 240 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
