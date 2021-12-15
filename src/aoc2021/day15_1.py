import logging
from typing import List

from aoc2021.day15_common import RiskProcessor


def process(risks: List[str]):
    # Parse risks
    p = RiskProcessor(risks)

    # Process best path
    logging.info(f"Result: {p.best_path()}.")
