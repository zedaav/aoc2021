import logging
from typing import List

from aoc2021.commons import dump_table

START = "start"
END = "end"


class Cave:
    def __init__(self, cave: str, small_visits: int):
        self.name = cave
        self.exits = set()
        self.is_big = all(c >= "A" and c <= "Z" for c in self.name)
        self.is_end = self.name == END
        self.is_start = self.name == START

        # Compute max visits
        if self.is_start or self.is_end:
            self.max_visits = 1
        elif self.is_big:
            self.max_visits = -1
        else:
            self.max_visits = small_visits

    def __repr__(self) -> str:
        return f"Cave(name: {self.name}; is_big: {self.is_big}; is_end: {self.is_end}; exits {[c.name for c in self.exits]}"


class PathBuilder:
    def __init__(self, start: Cave, used_nodes: List[Cave]) -> None:
        self.current = start
        self.used_nodes = used_nodes + [start]

    def follow_paths(self) -> list:
        # This a valid path only if we reached the end
        if self.current.is_end:
            return [self]

        # Choose among exits (filter already used ones)
        out = []
        for candidate in self.current.exits:
            c_count = self.used_nodes.count(candidate)
            # Handle small caves...
            if not candidate.is_big:
                # Already enough candidate?
                if c_count >= candidate.max_visits:
                    continue

                # If candidate may be present more than 1
                if candidate.max_visits > 1 and c_count == 1:
                    # Verify that there is not already a small cave with more than one
                    if any(not c.is_big and self.used_nodes.count(c) > 1 for c in self.used_nodes):
                        continue

            # Process others normally
            out.extend(PathBuilder(candidate, self.used_nodes).follow_paths())
        return out


class PathProcessor:
    def __init__(self, paths: List[str], small_visits: int):
        self.caves = {}
        for path in paths:
            a, b = tuple(path.split("-"))
            cave_a = self.create_cave(a, small_visits)
            cave_b = self.create_cave(b, small_visits)
            cave_a.exits.add(cave_b)
            cave_b.exits.add(cave_a)

        logging.debug(f"Found {len(self.caves)} caves")
        dump_table(self.caves.values())

    def create_cave(self, name, small_visits: int) -> Cave:
        if name not in self.caves:
            self.caves[name] = Cave(name, small_visits)
        return self.caves[name]

    def list_paths(self) -> List[PathBuilder]:
        # Build all paths
        paths = PathBuilder(self.caves[START], []).follow_paths()
        logging.debug(f"Found paths: {len(paths)}")
        return paths
