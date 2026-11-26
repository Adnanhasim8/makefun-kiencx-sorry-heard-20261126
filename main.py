"""Entry for make.fun u-kiencx-sorry-i-heard-that-wrong-1858c729.

Writes one line: the apology a smart speaker gives its owner after
mishearing "buy milk" as "buy a cow".

Python 3.13 standard library only. No network at run time.
"""

import argparse
import os
import sys

ENTRY = "Sorry, I heard 'buy milk' as 'buy a cow' — she's in the driveway."


def resolve_output_dir(args) -> str:
    if args.out:
        return args.out
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    return "/output"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Write the entry line.")
    parser.add_argument("--out", default=None,
                        help="Output directory (default: $MAKEFUN_OUTPUT_DIR or /output)")
    args = parser.parse_args(argv)

    out_dir = resolve_output_dir(args)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate assertions: exactly one line, 1-140 characters, non-empty.
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 140, f"entry must be 1-140 chars, got {len(ENTRY)}"

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Verify what was written matches the gate exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 140, "written entry outside 1-140 chars"
    assert "\n" not in written, "written entry is not a single line"
    return 0


if __name__ == "__main__":
    sys.exit(main())
