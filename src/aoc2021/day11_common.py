import logging
from typing import List, Set, Tuple

from aoc2021.commons import dump_table


class OctopusProcessor:
    def __init__(self, lines: List[str]):
        # Iterate on lines
        self.octopuses = [[int(c) for c in line] for line in lines]
        self.y_size = len(self.octopuses)
        self.x_size = len(self.octopuses[0])

    def find_adjacent_ones(self, y: int, x: int) -> List[Tuple[int, int]]:
        adjacent_ones = []
        if x < self.x_size - 1:
            # There is a right adjacent value
            adjacent_ones.append((y, x + 1))
            if y < self.y_size - 1:
                # There is a bottom right adjacent value
                adjacent_ones.append((y + 1, x + 1))
        if y < self.y_size - 1:
            # There is a bottom adjacent value
            adjacent_ones.append((y + 1, x))
            if x > 0:
                # There is a bottom left adjacent value
                adjacent_ones.append((y + 1, x - 1))
        if x > 0:
            # There is a left adjacent value
            adjacent_ones.append((y, x - 1))
            if y > 0:
                # There is a top left adjacent value
                adjacent_ones.append((y - 1, x - 1))
        if y > 0:
            # There is a top adjacent value
            adjacent_ones.append((y - 1, x))
            if x < self.x_size - 1:
                # There is a right adjacent value
                adjacent_ones.append((y - 1, x + 1))
        return adjacent_ones

    def propagate_flash(self, y: int, x: int) -> Set[Tuple[int, int]]:
        # Increase energy by one
        was_flashed = self.octopuses[y][x] > 9
        self.octopuses[y][x] += 1

        # Flash?
        flashes = set()
        if not was_flashed and self.octopuses[y][x] > 9:
            # Propagate flash to all adjacent octopuses
            flashes.add((y, x))
            for y_a, x_a in self.find_adjacent_ones(y, x):
                flashes.update(self.propagate_flash(y_a, x_a))

        return flashes

    def process_flash(self) -> Set[Tuple[int, int]]:
        # Iterate on octopuses
        flash_locs = set()
        for y in range(self.y_size):
            for x in range(self.x_size):
                # Initiate flash sequence
                flash_locs.update(self.propagate_flash(y, x))

        # Reset flash energy to 0
        for y_f, x_f in flash_locs:
            self.octopuses[y_f][x_f] = 0

        return flash_locs

    def process_steps(self, steps: int) -> int:
        flashes = 0
        # Iterate on steps
        dump_table(self.octopuses)
        for step in range(1, steps + 1):
            # Iterate on octopuses
            flash_locs = self.process_flash()

            # Count flashes
            flashes += len(flash_locs)

            logging.debug(f"After step {step}:")
            dump_table(self.octopuses)

        return flashes

    def full_flash(self) -> int:
        steps = 0
        full_flash = False

        # Loop until full flash
        while not full_flash:
            steps += 1

            # Iterate on octopuses
            flash_locs = self.process_flash()

            # Verify full flash
            full_flash = len(flash_locs) == self.x_size * self.y_size

        return steps
