import logging
from typing import List

from aoc2021.day04_common import check_board, parse_inputs


def process(instructions: List[str]):
    # Parse inputs
    random_numbers, boards = parse_inputs(instructions)

    # Loop on numbers to mark boards
    result = None
    for number in random_numbers:  # pragma: no branch
        for board in boards:
            result = check_board(board, number)
            if result is not None:
                break
        if result is not None:
            break

    # Final position
    logging.info(f"Result: {result}.")
