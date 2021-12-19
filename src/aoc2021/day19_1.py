import logging
from typing import List

from aoc2021.day19_common import locate_all_beacons, parse_scanners


def process(scanners: List[str]):
    # Process scanners & beacons
    scanners = parse_scanners(scanners)

    # Find all common beacons
    locate_all_beacons(scanners)

    # Count all beacons
    all_beacons = set()
    for s in filter(lambda s: s.known_pos, scanners):
        all_beacons.update(s.beacons)
    logging.info(f"Result: {len(all_beacons)}.")
