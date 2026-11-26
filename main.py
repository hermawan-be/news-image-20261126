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
    # The infographic is the whole entry: refuse to continue if it is missing,
    # so a broken build fails here instead of silently producing an empty output.
    if not os.path.isfile(source):
        print("missing entry image: {}".format(source), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print("copied {} -> {}".format(source, target))
    print("done: entry image ready in {}".format(out_dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
