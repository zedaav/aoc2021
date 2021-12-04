import logging
from typing import List


def process(input_lines: List[str]):
    # All lines are ints
    values = [int(line) for line in input_lines]

    # Compute measurements increments
    increments = 0
    for index in range(3, len(values)):
        previous_sum = values[index - 3] + values[index - 2] + values[index - 1]
        new_sum = values[index - 2] + values[index - 1] + values[index - 0]
        if new_sum > previous_sum:
            increments += 1
    logging.info(f"Result: {increments}.")
