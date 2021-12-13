import logging
from typing import List

from aoc2021.day13_common import PaperProcessor


def process(instructions: List[str]):
    # Parse instructions
    p = PaperProcessor(instructions)

    # Process folds
    p.fold(1)
    logging.info(f"Result: {p.count()}.")
