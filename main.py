"""Copy the news infographic into the bounty output directory.

Reads MAKEFUN_OUTPUT_DIR (defaults to /output), creates it if needed,
and copies entry.png next to this script into that directory.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print("copied {} -> {}".format(source, target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
