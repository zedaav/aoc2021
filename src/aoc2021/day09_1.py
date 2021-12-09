import logging
from typing import List

from aoc2021.day09_commons import find_lowpoints


def process(heights: List[str]):
    # Build low_points
    low_points = find_lowpoints(heights)
    logging.debug(f"Lowpoints ({len(low_points)}): {low_points}")

    # Build risk sum
    risk = len(low_points) + sum([int(heights[y][x]) for y, x in low_points])
    logging.info(f"Result: {risk}.")
