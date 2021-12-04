import logging
from typing import List

from aoc2021.day04_common import check_board, parse_inputs


def process(instructions: List[str]):
    # Parse inputs
    random_numbers, boards = parse_inputs(instructions)

    # Loop on numbers to mark boards
    won_boards = set()
    for number in random_numbers:  # pragma: no branch
        for index in range(len(boards)):
            result = check_board(boards[index], number)
            if result is not None:
                # Board won, remember it
                won_boards.add(index)

                # Last board to win?
                if len(won_boards) == len(boards):
                    break

        # Last board to win?
        if len(won_boards) == len(boards):
            break

    # Final position
    logging.info(f"Result: {result}.")
