import logging
from typing import List

from aoc2021.day14_common import PolymerProcessor


def process(instructions: List[str]):
    # Parse instructions
    p = PolymerProcessor(instructions)

    # Process polymer
    p.process(40)
    logging.info(f"Result: {p.count()}.")
