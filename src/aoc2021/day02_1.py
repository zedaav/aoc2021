import logging
import re
from typing import List

FORWARD_PATTERN = re.compile("forward ([0-9]+)")
DOWN_PATTERN = re.compile("down ([0-9]+)")
UP_PATTERN = re.compile("up ([0-9]+)")
PATTERNS = [FORWARD_PATTERN, DOWN_PATTERN, UP_PATTERN]


def process(instructions: List[str]):
    # Loop on instructions
    horizontal = depth = 0
    for instruction in instructions:
        for pattern in PATTERNS:  # pragma: no branch
            m = pattern.match(instruction)

            # Match?
            if m is not None:
                offset = int(m.group(1))

                # Update position
                if m.re == FORWARD_PATTERN:
                    horizontal += offset
                elif m.re == DOWN_PATTERN:
                    depth += offset
                else:  # m.re == UP_PATTERN
                    depth -= offset

                # Nothing more to do with patterns
                break

    # Final position
    logging.info(f"Result: {horizontal * depth}.")
