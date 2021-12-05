import logging
import re
from typing import List, Tuple

LINE_PATTERN = re.compile("([0-9]+),([0-9]+) +-> +([0-9]+),([0-9]+)")


def parse_lines(inputs: List[str]) -> Tuple[int, int, List[Tuple[Tuple[int, int], Tuple[int, int]]]]:
    # Browse input lines
    out = []
    width = height = 0
    for line in inputs:
        m = LINE_PATTERN.match(line)
        if m is not None:  # pragma: no branch
            x1, y1, x2, y2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
            out.append(((x1, y1), (x2, y2)))
            width = max([width, x1 + 1, x2 + 1])
            height = max([width, y1 + 1, y2 + 1])
    return width, height, out


def build_table(width: int, height: int, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    # Prepare empty coverage table
    table = [[0 for _w in range(width)] for _l in range(height)]

    # Fill with lines
    for line in lines:
        # Vertical or horizontal line?
        (x1, y1), (x2, y2) = line
        if x1 == x2:
            # Vertical one
            start = min([y1, y2])
            end = max([y1, y2])
            logging.debug(f"Draw vertical line; x: {x1}; y: {start}->{end}")
            for index in range(start, end + 1):
                table[index][x1] += 1
        elif y1 == y2:
            # Horizontal one
            start = min([x1, x2])
            end = max([x1, x2])
            logging.debug(f"Draw horizontal line; x: {start}->{end}; y: {y1}")
            for index in range(start, end + 1):
                table[y1][index] += 1
        else:
            # Diagonal one
            delta = abs(x1 - x2) + 1
            v_offset = 1 if y2 > y1 else -1
            h_offset = 1 if x2 > x1 else -1
            logging.debug(f"Draw diagonal line; x: {x1}->{x2} ({h_offset}); y: {y1}->{y2} ({v_offset})")
            for index in range(0, delta):
                table[y1 + (v_offset * index)][x1 + (h_offset * index)] += 1
    return table
