import logging
import re
from typing import Dict, List, Tuple

from aoc2021.commons import dump_table

BOARD_PATTERN = re.compile("([0-9]+) +([0-9]+) +([0-9]+) +([0-9]+) +([0-9]+)")


def check_board(board: List[Dict[int, bool]], number: int) -> int:
    # Mark number in board (if any)
    for board_line in board:
        if number in board_line:
            board_line[number] = True
            logging.debug(f"Board match for {number}!")
            dump_table(board)

    # Browse board to check if at least one line or one column is fully marked
    if any(all(v for v in board_line.values()) for board_line in board) or any(all(list(board_line.values())[i] for board_line in board) for i in range(5)):
        # Bingo!
        logging.debug("Bingo!")
        # Now find all non-marked numbers
        remaining_numbers = []
        for board_line in board:
            remaining_numbers.extend(map(lambda t: t[0], filter(lambda t: not t[1], board_line.items())))

        # Final result is triggering number x sum of remaining numbers
        return number * sum(remaining_numbers)

    # Not bingo yet...
    return None


def append_board(new_board: List[Dict[int, bool]], boards: List[List[Dict[int, bool]]]) -> bool:
    if new_board is not None:
        logging.debug("New board!")
        dump_table(new_board)
        boards.append(new_board)
        return True
    return False


def parse_inputs(instructions: List[str]) -> Tuple[List[int], List[List[Dict[int, bool]]]]:
    # Get random numbers
    random_numbers = [int(nb) for nb in instructions[0].split(",")]
    logging.debug(f"Random numbers: {random_numbers}")

    # Loop to build boards
    boards = []
    new_board = None
    for line in instructions[1:]:
        m = BOARD_PATTERN.search(line)
        if m is None:
            # Separating line, remember board
            if append_board(new_board, boards):
                new_board = None
        else:
            # Board line
            if new_board is None:
                new_board = []
            new_board.append({int(m.group(i)): False for i in range(1, 6)})
    append_board(new_board, boards)
    return random_numbers, boards
