import logging
from typing import List

from aoc2021.day21_common import parse_positions


def process(lines: List[str]):
    # Process positions
    g = parse_positions(lines)

    # Get final score
    logging.info(f"Result: {g.play_deter(1000)}.")
