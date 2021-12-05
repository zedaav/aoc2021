import logging
from typing import List

from aoc2021.commons import dump_table
from aoc2021.day05_common import build_table, parse_lines


def process(instructions: List[str]):
    # Parse lines tuples
    width, height, all_lines = parse_lines(instructions)

    # Filter horizontal/vertical lines
    filtered_lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], all_lines))
    logging.debug("Filtered lines:")
    dump_table(filtered_lines)

    # Build coverage table
    coverage_table = build_table(width, height, filtered_lines)
    logging.debug("Final table state:")
    dump_table(coverage_table)

    # Count overlapping points
    overlaps = [x for line in coverage_table for x in filter(lambda o: o > 1, line)]
    logging.info(f"Result: {len(overlaps)}.")
