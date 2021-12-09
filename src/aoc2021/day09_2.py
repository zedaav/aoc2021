import logging
from typing import List, Tuple

from aoc2021.day09_commons import find_adjacent_ones, find_lowpoints


def find_basin_points(y: int, x: int, basin_points: List[Tuple[int, int]], heights: List[str]):
    # Compute all adjacent ones, which are not already count as a basin point, and not a '9'
    new_adjacent_ones = list(filter(lambda t: t not in basin_points and heights[t[0]][t[1]] != "9", find_adjacent_ones(y, x, heights)))
    basin_points.extend(new_adjacent_ones)

    # Also compute basin points for all new basin points
    for new_y, new_x in new_adjacent_ones:
        find_basin_points(new_y, new_x, basin_points, heights)


def process(heights: List[str]):
    # Build low_points
    low_points = find_lowpoints(heights)
    logging.debug(f"Lowpoints ({len(low_points)}): {low_points}")

    # Find basins
    basin_sizes = []
    for y, x in low_points:
        basin_points = [(y, x)]
        find_basin_points(y, x, basin_points, heights)
        logging.debug(f"New basin (size: {len(basin_points)}): {basin_points}")

        # Remember basin size
        basin_sizes.append(len(basin_points))

    # Multiply three biggest basins
    basin_sizes.sort(reverse=True)
    logging.debug(f"3 biggest basin sizes: {basin_sizes[:3]}")
    result = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    logging.info(f"Result: {result}.")
