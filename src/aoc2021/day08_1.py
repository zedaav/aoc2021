import logging
from typing import List

from aoc2021.day08_commons import parse_patterns

# Unique lens
UNIQUE_LENS = [2, 4, 3, 7]  # for 1, 4, 7, 8 patterns of 7-segments displays


def process(instructions: List[str]):
    # Build patterns
    patterns = parse_patterns(instructions)

    # Count unique number of segments
    unique_count = 0
    for _pattern, outputs in patterns:
        new_count = len(list((filter(lambda x: len(x) in UNIQUE_LENS, outputs))))
        logging.debug(f"{outputs} --> {new_count}")
        unique_count += new_count

    # Minimum cost
    logging.info(f"Result: {unique_count}.")
