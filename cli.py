#!/usr/bin/env python3

import argparse
import sys
from core.scaffold import run as run_scaffold

def main():
    parser = argparse.ArgumentParser(
        description="SDK Core Command Line Interface"
    )

    subparsers = parser.add_subparsers(
        title="Commands",
        dest="command",
        required=True
    )

    # scaffold command
    scaffold_parser = subparsers.add_parser(
        "scaffold",
        help="Create a new project scaffold"
    )
    scaffold_parser.add_argument(
        "--name",
        required=True,
        help="Name of the new project"
    )

    args = parser.parse_args()

    if args.command == "scaffold":
        run_scaffold(args.name)
    else:
        print("Unknown command. Use --help for guidance.")
        sys.exit(1)

if __name__ == "__main__":
    main()
