#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one funny single-line sick-day excuse to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, stdlib only, no network.
"""

import os
import shutil
import sys

EXCUSE = (
    "I woke up and my left leg has decided it's freelance now, "
    "so I'm working from the couch until it signs a new contract."
)


def clear_output_dir(path: str) -> None:
    """Remove only the CONTENTS of the output dir, never the dir itself.

    The grader may run with a root-owned output dir inside a sticky parent,
    where deleting the dir itself fails with EPERM.
    """
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.islink(target) or os.path.isfile(target):
            os.unlink(target)
        elif os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.unlink(target)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    clear_output_dir(out_dir)
    entry_path = os.path.join(out_dir, "entry.txt")
    data = EXCUSE.encode("utf-8")
    with open(entry_path, "wb") as fh:
        fh.write(data)
    # Read back and verify: the file must hold exactly these bytes, no
    # trailing newline, byte count == character count.
    with open(entry_path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("entry.txt verification failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
