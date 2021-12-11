import logging
from typing import List

from aoc2021.day11_common import OctopusProcessor


def process(lines: List[str]):
    # Parse octopuses
    p = OctopusProcessor(lines)

    # Process with flashes
    flashes = p.process_steps(100)
    logging.info(f"Result: {flashes}.")
