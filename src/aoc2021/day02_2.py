#!/usr/bin/env python3
import re
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List

FORWARD_PATTERN = re.compile("forward ([0-9]+)")
DOWN_PATTERN = re.compile("down ([0-9]+)")
UP_PATTERN = re.compile("up ([0-9]+)")
PATTERNS = [FORWARD_PATTERN, DOWN_PATTERN, UP_PATTERN]


def day02_2(input_args: List[str]):
    # Parse args
    parser = ArgumentParser(description="Solution for AoC 2021 day 2-2")
    parser.add_argument("input", type=Path, nargs=1, help="Path to input file")
    args = parser.parse_args(input_args)

    # Read file
    input_file: Path = args.input[0]
    with input_file.open() as f:
        instructions = f.readlines()

    # Loop on instructions
    horizontal = depth = aim = 0
    for instruction in instructions:
        for pattern in PATTERNS:  # pragma: no branch
            m = pattern.match(instruction)

            # Match?
            if m is not None:
                offset = int(m.group(1))

                # Update position
                if m.re == FORWARD_PATTERN:
                    horizontal += offset
                    depth += offset * aim
                elif m.re == DOWN_PATTERN:
                    aim += offset
                else:  # m.re == UP_PATTERN
                    aim -= offset

                # Nothing more to do with patterns
                break

    # Final position
    print(f"Result: {horizontal * depth}.")


def main():  # pragma: no cover
    day02_2(sys.argv[1:])


if __name__ == "__main__":  # pragma: no cover
    main()
