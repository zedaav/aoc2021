import logging
from typing import List

from aoc2021.day18_common import parse_numbers


def process(numbers: List[str]):
    # Process numbers
    numbers = parse_numbers(numbers)

    # Iterate on numbers
    n = numbers[0]
    logging.debug(f">> {n}")
    for other in numbers[1:]:
        n = n + other
        n.reduce()
        logging.debug(f" >> {n}")

    # Finally get magnitude
    logging.info(f"Result: {n.magnitude()}.")
