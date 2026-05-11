"""Run the E1 direct-generation baseline template.

This script keeps a clear CLI entry point for E1. The current public runtime
uses the case-based runner; disabling all internal agents requires additional
integration and is therefore reported explicitly.
"""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="E1 Bare Model baseline template.")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--letters", nargs="+", default=["A"])
    parser.add_argument("--result-root", default="./results")
    args = parser.parse_args()

    print("E1 Bare Model is provided as an experiment template.")
    print("Requested range: %s-%s, letters=%s" % (args.start, args.end, ",".join(args.letters)))
    print("This setting requires a direct-generation runner that bypasses the multi-agent pipeline.")
    print("No benchmark results were generated.")
    return 2


if __name__ == "__main__":
    sys.exit(main())

