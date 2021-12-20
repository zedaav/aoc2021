import logging
from typing import List

from aoc2021.day20_common import parse_instructions


def process(lines: List[str]):
    # Process algo + image
    p = parse_instructions(lines)

    # Apply algo 50 times
    p.process(50)

    # Count lit pixels
    logging.info(f"Result: {p.pixels}.")
