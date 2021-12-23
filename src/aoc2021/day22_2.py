import logging
from typing import List

from aoc2021.day22_common import Reactor


def process(steps: List[str]):
    # Process steps
    r = Reactor(steps)

    # Get final score
    logging.info(f"Result: {r.process(None)}.")
