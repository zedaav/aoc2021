import logging
import re
from pathlib import Path
from typing import List

DOT_PATTERN = re.compile("([0-9]+),([0-9]+)")
FOLD_PATTERN = re.compile("fold along ([xy])=([0-9]+)")


class PaperProcessor:
    def __init__(self, instructions: List[str]):
        # Iterate on instructions
        self.dot_coords = []
        self.folds = []
        for instruction in instructions:
            m = DOT_PATTERN.match(instruction)
            if m is not None:
                self.dot_coords.append((int(m.group(1)), int(m.group(2))))
            else:
                m = FOLD_PATTERN.match(instruction)
                if m is not None:
                    self.folds.append((m.group(1), int(m.group(2))))

        # Build dots map
        self.dots = [[False for x in range(max(c[0] for c in self.dot_coords) + 1)] for y in range(max(c[1] for c in self.dot_coords) + 1)]
        for x, y in self.dot_coords:
            self.dots[y][x] = True

        # Dump dots initial state
        self.dump(0)

    def fold_left(self, fold_pos: int):
        # Fold left
        width = len(self.dots[0])
        if fold_pos >= width / 2:
            new_width = fold_pos  # Final width of the new line
            overlapping_size = width - fold_pos - 1  # Size on which folded parts are overlapping
            start_left = True
        else:
            new_width = width - fold_pos - 1  # Final width of the new line
            overlapping_size = fold_pos  # Size on which folded parts are overlapping
            start_left = False
        non_overlapping_size = new_width - overlapping_size
        logging.debug(
            f"fold_pos: {fold_pos} / new_width: {new_width} / overlapping_size: {overlapping_size} / start_left: {start_left} / non_overlapping_size: {non_overlapping_size}"
        )

        new_dots = []
        for line in self.dots:
            new_line = []
            if start_left:
                # Start with far-left dots
                for i in range(non_overlapping_size):
                    new_line.append(line[i])
                # Continue with overlapping dots
                for i in range(overlapping_size):
                    new_line.append(line[i + non_overlapping_size] or line[-(i + 1)])
            else:
                # Start with far-right dots (reversed)
                for i in range(non_overlapping_size):
                    new_line.append(line[-(i + 1)])  # pragma: no cover
                # Continue with overlapping dots
                for i in range(overlapping_size):
                    new_line.append(line[i] or line[-(i + non_overlapping_size + 1)])

            new_dots.append(new_line)
        return new_dots

    def fold_up(self, fold_pos: int):
        # Fold up
        height = len(self.dots)
        if fold_pos >= height / 2:
            new_height = fold_pos  # Final height of the new column
            overlapping_size = height - fold_pos - 1  # Size on which folded parts are overlapping
            start_top = True
        else:
            new_height = height - fold_pos - 1  # Final height of the new column
            overlapping_size = fold_pos  # Size on which folded parts are overlapping
            start_top = False
        non_overlapping_size = new_height - overlapping_size
        width = len(self.dots[0])
        logging.debug(
            f"width: {width} / fold_pos: {fold_pos} / new_height: {new_height} / overlapping_size: {overlapping_size} / start_top: {start_top} / non_overlapping_size: {non_overlapping_size}"
        )

        new_dots = [[] for line_index in range(new_height)]
        for x in range(width):
            if start_top:
                # Start with far-top dots
                for i in range(non_overlapping_size):
                    new_dots[i].append(self.dots[i][x])
                # Continue with overlapping dots
                for i in range(overlapping_size):
                    new_dots[i + non_overlapping_size].append(self.dots[i + non_overlapping_size][x] or self.dots[-(i + 1)][x])
            else:
                # Start with far-bottom dots (reversed)
                for i in range(non_overlapping_size):
                    new_dots[i].append(self.dots[-(i + 1)][x])  # pragma: no cover
                # Continue with overlapping dots
                for i in range(overlapping_size):
                    new_dots[i + non_overlapping_size].append(self.dots[i][x] or self.dots[-(i + non_overlapping_size + 1)][x])
        return new_dots

    def fold(self, count: int):
        # Iterate on fold instructions
        for fold_index in range(count if count > 0 else len(self.folds)):
            # X or Y
            way, fold_pos = self.folds[fold_index]
            if way == "x":
                self.dots = self.fold_left(fold_pos)
            else:
                self.dots = self.fold_up(fold_pos)

            # One more fold
            logging.debug(f"after {fold_index+1} fold(s):")
            self.dump(fold_index + 1)

    def dump(self, step: int):
        logging.debug(f"Dots ({len(self.dots[0])}x{len(self.dots)})")
        out = Path() / "out"
        out.mkdir(parents=True, exist_ok=True)
        with (out / f"dump13-{step}.txt").open("w") as f:
            for dot_line in self.dots:
                f.write("".join("#" if d else "." for d in dot_line) + "\n")

    def count(self):
        # Count all dots
        return sum([sum([1 if d else 0 for d in line]) for line in self.dots])
