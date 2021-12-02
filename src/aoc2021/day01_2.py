#!/usr/bin/env python3
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List


def day01_2(input_args: List[str]):
    # Parse args
    parser = ArgumentParser(description="Solution for AoC 2021 day 1-2")
    parser.add_argument("input", type=Path, nargs=1, help="Path to input file")
    args = parser.parse_args(input_args)

    # Read file
    input_file: Path = args.input[0]
    with input_file.open() as f:
        values = [int(line) for line in f.readlines()]

    # Compute measurements increments
    increments = 0
    for index in range(3, len(values)):
        previous_sum = values[index - 3] + values[index - 2] + values[index - 1]
        new_sum = values[index - 2] + values[index - 1] + values[index - 0]
        if new_sum > previous_sum:
            increments += 1
    print(f"Result: {increments}.")


def main():  # pragma: no cover
    day01_2(sys.argv[1:])


if __name__ == "__main__":  # pragma: no cover
    main()
