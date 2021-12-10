import logging
from typing import List

from aoc2021.day10_common import parse_lines

# Corrupted closer points
CORRUPTED_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def process(lines: List[str]):
    # Parse lines
    corrupted_chars, _ = parse_lines(lines)

    # Build error score
    score = sum(CORRUPTED_POINTS[c] for c in corrupted_chars.values())
    logging.info(f"Result: {score}.")
