import logging
from typing import List

from aoc2021.day06_common import process_fishes, process_fishes_simple


def process(instructions: List[str]):
    # Read fishes initial states
    fishes = [int(x) for x in instructions[0].split(",")]
    logging.debug(f"Initial fishes count: {len(fishes)}: {fishes}")

    # Count fishes
    logging.info(f"ResultOld: {process_fishes_simple(list(fishes), 80)}.")
    logging.info(f"Result: {process_fishes(fishes, 80)}.")
