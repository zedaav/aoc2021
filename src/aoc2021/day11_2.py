import logging
from typing import List

from aoc2021.day11_common import OctopusProcessor


def process(lines: List[str]):
    # Parse octopuses
    p = OctopusProcessor(lines)

    # Count steps until full flash
    steps = p.full_flash()
    logging.info(f"Result: {steps}.")
