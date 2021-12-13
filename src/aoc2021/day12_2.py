import logging
from typing import List

from aoc2021.day12_common import PathProcessor


def process(paths: List[str]):
    # Parse paths
    p = PathProcessor(paths, 2)

    # Process paths
    logging.info(f"Result: {len(p.list_paths())}.")
