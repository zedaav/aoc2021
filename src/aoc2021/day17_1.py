import logging
from typing import List

from aoc2021.day17_common import TargetProcessor


def process(inputs: List[str]):
    # Process target
    p = TargetProcessor(inputs[0])

    # Give a try
    logging.info(f"Result: {max(p[1] for trj in p.trajectories() for p in trj.points)}.")
