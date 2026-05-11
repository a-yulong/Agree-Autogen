"""Run the E1 Bare Model baseline entry point.

The current public runtime does not yet expose the switches needed to bypass
all multi-agent stages safely. This script therefore reports an explicit
unsupported status instead of producing artificial results.
"""

import argparse
import sys
from pathlib import Path


DEFAULT_CONFIG = Path(__file__).resolve().parent / "configs" / "e1_bare_model.yaml"


def main() -> int:
    parser = argparse.ArgumentParser(description="E1 Bare Model baseline template.")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--letters", nargs="+", default=["A"])
    parser.add_argument("--result-root", default="./results")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    args = parser.parse_args()

    print("E1 Bare Model is not executable in the current public runtime.")
    print(f"Config: {args.config}")
    print("Requested range: %s-%s, letters=%s" % (args.start, args.end, ",".join(args.letters)))
    print("Required runtime switch: direct_generation_runner")
    print("No benchmark results were generated.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
