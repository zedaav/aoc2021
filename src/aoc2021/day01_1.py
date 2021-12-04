import logging
from typing import List


def process(input_lines: List[str]):
    # All lines are ints
    values = [int(line) for line in input_lines]

    # Compute measurements increments
    increments = 0
    for index in range(1, len(values)):
        if values[index] > values[index - 1]:
            increments += 1
    logging.info(f"Result: {increments}.")
