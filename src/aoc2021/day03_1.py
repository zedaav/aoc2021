#!/usr/bin/env python3
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List


def day03_1(input_args: List[str]):
    # Parse args
    parser = ArgumentParser(description="Solution for AoC 2021 day 3-1")
    parser.add_argument("input", type=Path, nargs=1, help="Path to input file")
    args = parser.parse_args(input_args)

    # Read file
    input_file: Path = args.input[0]
    with input_file.open() as f:
        lines = [line.strip("\r\n ") for line in f.readlines()]
        diagnostics = [int("0b" + line, base=0) for line in lines]

    # Loop on diagnostics
    diag_count = len(diagnostics)
    sample_size = len(lines[0])
    print(f"sample size: {sample_size}")
    gamma_bits = {i: [] for i in range(sample_size)}
    for diagnostic in diagnostics:
        for i in range(sample_size):
            bit = (diagnostic >> i) & 1
            gamma_bits[i].append(bit)

    # Reckon gamma
    gamma = 0
    for i in range(sample_size):
        ones_count = sum(gamma_bits[i])

        # Corner case: exactly same number of 1s & 0s
        assert ones_count != diag_count / 2, f"Don't known what to do at index {i}: {ones_count} 1s on {diag_count} diagnostics"

        gamma |= (1 if (ones_count > diag_count / 2) else 0) << i

    # Epsilon is gamma complement to 2
    epsilon = gamma ^ sum(1 << i for i in range(sample_size))

    # Final power consumption
    print(f"gamma: {gamma} ({bin(gamma)})")
    print(f"epsilon: {epsilon} ({bin(epsilon)})")
    print(f"Result: {gamma * epsilon}.")


def main():  # pragma: no cover
    day03_1(sys.argv[1:])


if __name__ == "__main__":  # pragma: no cover
    main()
