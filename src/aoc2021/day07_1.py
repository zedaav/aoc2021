import logging
from typing import List

from aoc2021.day07_common import factorize_crabs


def process(instructions: List[str]):
    # Read crabs initial states
    crabs = [int(x) for x in instructions[0].split(",")]
    logging.debug(f"Initial crabs count: {len(crabs)}")

    # Iterate first to factorize per initial pos + find min/max
    min_pos, max_pos, crabs_map = factorize_crabs(crabs)

    # Reckon all fuel cost possibilities
    costs = {}
    for candidate in range(min_pos, max_pos + 1):
        costs[candidate] = sum([abs(pos - candidate) * count for pos, count in crabs_map.items()])

    # Minimum cost
    logging.info(f"Result: {min(costs.values())}.")
