from typing import List, Tuple


def find_adjacent_ones(y: int, x: int, heights: List[str]) -> List[Tuple[int, int]]:
    y_size = len(heights)
    x_size = len(heights[0])
    adjacent_ones = []
    if x < x_size - 1:
        # There is a right adjacent value
        adjacent_ones.append((y, x + 1))
    if y < y_size - 1:
        # There is a bottom adjacent value
        adjacent_ones.append((y + 1, x))
    if x > 0:
        # There is a left adjacent value
        adjacent_ones.append((y, x - 1))
    if y > 0:
        # There is a top adjacent value
        adjacent_ones.append((y - 1, x))
    return adjacent_ones


def find_lowpoints(heights: List[str]) -> List[Tuple[int, int]]:
    # Browse heights in both ways
    y_size = len(heights)
    x_size = len(heights[0])
    low_points = []
    for y in range(y_size):
        for x in range(x_size):
            # Find adjacent points
            adjacent_ones = find_adjacent_ones(y, x, heights)

            # This is a low point if inferior to all its adjacent values
            if heights[y][x] < min(heights[ay][ax] for ay, ax in adjacent_ones):
                low_points.append((y, x))

    return low_points
