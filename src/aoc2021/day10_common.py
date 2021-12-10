import logging
from typing import Dict, List, Tuple

# Valid delimiters
DELIMITERS = {"(": ")", "{": "}", "[": "]", "<": ">"}


def parse_lines(lines: List[str]) -> Tuple[Dict[int, str], Dict[int, str]]:
    # Iterate on lines
    corrupted_chars = {}
    missing_closers = {}
    for index in range(len(lines)):
        line = lines[index]

        # Iterate on chars
        opening_stack = []
        for char in line:
            assert char in DELIMITERS.keys() or char in DELIMITERS.values()

            # Opening delimiter?
            if char in DELIMITERS.keys():
                # One more opening char
                opening_stack.append(char)
            else:
                # Closing one; check for matching
                last_opener = opening_stack.pop(-1)
                expected_closer = DELIMITERS[last_opener]
                if char != expected_closer:
                    # Corrupted line
                    logging.debug(f"Line {index}: corrupted (expected '{expected_closer}' but got '{char}')")
                    corrupted_chars[index] = char
                    break

        # If not a corrupted line, but still getting chars in the opening stack, remember missing closers
        if index not in corrupted_chars and len(opening_stack):
            opening_stack.reverse()
            missing_closers[index] = [DELIMITERS[o] for o in opening_stack]
            logging.debug(f"Line {index}: incomplete (missing '{missing_closers[index]}' closers)")

    return corrupted_chars, missing_closers
