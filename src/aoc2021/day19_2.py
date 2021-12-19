import logging
from typing import List

from aoc2021.day19_common import locate_all_beacons, parse_scanners


def process(scanners: List[str]):
    # Process scanners & beacons
    scanners = parse_scanners(scanners)

    # Find all common beacons
    locate_all_beacons(scanners)

    # Reckon all manhattan distances
    all_scanners = range(len(scanners))
    all_distances = set()
    for index in all_scanners:
        others = list(all_scanners)
        others.remove(index)
        scanner1 = scanners[index].coords
        for other in others:
            scanner2 = scanners[other].coords
            all_distances.add(abs(scanner1[0] - scanner2[0]) + abs(scanner1[1] - scanner2[1]) + abs(scanner1[2] - scanner2[2]))
    logging.info(f"Result: {max(all_distances)}.")
