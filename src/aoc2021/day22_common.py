import logging
import re
from collections import Counter
from math import prod
from typing import List, Tuple

INSTRUCTION_PATTERN = re.compile("(o[nf]+) x=([-0-9]+)..([-0-9]+),y=([-0-9]+)..([-0-9]+),z=([-0-9]+)..([-0-9]+)")


def reckon_inter(
    cub1: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]], cub2: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    # Iterate on couples
    inter = [(max(a1, b1), min(a2, b2)) for (a1, a2), (b1, b2) in zip(cub1, cub2)]
    if all(a1 <= a2 for a1, a2 in inter):
        inter = tuple(inter)
        logging.debug(f"Intersection of {cub1} and {cub2} is {inter}")
        return inter

    # If intersection coords are reversed on at least one axis, cuboids don't have any intersection
    return None


def reckon_volume(span: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]) -> int:
    return prod(abs(c1 - c2) + 1 for c1, c2 in span)


class Reactor:
    def __init__(self, steps: List[str]):
        # Build all instruction cubes
        self.steps = {}
        for m in filter(lambda m: m is not None, (map(INSTRUCTION_PATTERN.match, steps))):
            x1, x2, y1, y2, z1, z2 = tuple(int(m.group(i)) for i in range(2, 2 + 6))
            self.steps[((x1, x2), (y1, y2), (z1, z2))] = True if m.group(1) == "on" else False

    def process(self, limit: int) -> int:
        cuboids = Counter()
        for span, on_off in self.steps.items():
            logging.debug(f"process: {span}")
            (x1, x2), (y1, y2), (z1, z2) = span
            if limit is not None:
                # Simply ignore if at least one couple is ont of limit
                if any(abs(c1) > limit and abs(c2) > limit for c1, c2 in span):
                    continue

                # Apply limit
                x1, x2, y1, y2, z1, z2 = tuple(map(lambda c: min(c, limit) if limit > 0 else max(c, limit), (x1, x2, y1, y2, z1, z2)))
                span = ((x1, x2), (y1, y2), (z1, z2))
                logging.debug(f"after limit: {span}")

            # Handle intersections
            for cuboid, flag in cuboids.copy().items():
                inter = reckon_inter(cuboid, span)
                if inter is not None:
                    cuboids[inter] += -flag

            if on_off:
                # Turn on this cuboid
                cuboids[span] += 1

            # Reduce 0-count cuboids
            cuboids = Counter({c: f for c, f in cuboids.items() if f})
        return sum(flag * reckon_volume(c) for c, flag in cuboids.items())
