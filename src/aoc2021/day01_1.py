#!/usr/bin/env python3
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List


def day01_1(input_args: List[str]):
    # Parse args
    parser = ArgumentParser(description="Solution for AoC 2021 day 1-1")
    parser.add_argument("input", type=Path, nargs=1, help="Path to input file")
    args = parser.parse_args(input_args)

    # Read file
    input_file: Path = args.input[0]
    with input_file.open() as f:
        values = [int(line) for line in f.readlines()]

    # Compute measurements increments
    increments = 0
    for index in range(1, len(values)):
        if values[index] > values[index - 1]:
            increments += 1
    print(f"Result: {increments}.")


def main():  # pragma: no cover
    day01_1(sys.argv[1:])


if __name__ == "__main__":  # pragma: no cover
    main()
