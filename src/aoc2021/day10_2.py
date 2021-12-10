import logging
from typing import List

from aoc2021.day10_common import parse_lines

# Missing closer points
CLOSER_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def process(lines: List[str]):
    # Parse lines
    _, missing_closers = parse_lines(lines)

    # Build error score
    all_scores = []
    for missing_sample in missing_closers.values():
        score = 0
        for sample in missing_sample:
            score = score * 5 + CLOSER_POINTS[sample]
        all_scores.append(score)

    # Take the middle score
    assert len(all_scores) % 2 == 1
    all_scores.sort()
    logging.info(f"Result: {all_scores[int(len(all_scores)/2)]}.")
