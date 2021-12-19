import logging
from typing import List

from aoc2021.day18_common import parse_numbers


def process(numbers: List[str]):
    # Process numbers
    numbers = parse_numbers(numbers)

    # Find all magnitudes for all permutations
    all_indexes = range(len(numbers))
    magnitudes = []
    for c_index1 in all_indexes:
        others = list(all_indexes)
        others.remove(c_index1)
        for c_index2 in others:
            addition = numbers[c_index1] + numbers[c_index2]
            addition.reduce()
            magnitude = addition.magnitude()
            magnitudes.append(magnitude)

    # Finally get magnitude
    logging.info(f"Result: {max(magnitudes)}.")
