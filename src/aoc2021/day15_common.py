import heapq
from typing import List, Tuple


class RiskProcessor:
    def __init__(self, risks: List[str], tiles: int = 1):
        # Parse risks
        self.risks = [[(int(c) - 1 + delta_x + delta_y) % 9 + 1 for delta_x in range(tiles) for c in line] for delta_y in range(tiles) for line in risks]
        self.y_size = len(self.risks)
        self.x_size = len(self.risks[0])
        self.best_paths = [[None] * self.x_size for _ in range(self.y_size)]
        self.best_paths[0][0] = 0

    def find_adjacent_ones(self, y: int, x: int) -> List[Tuple[int, int]]:
        adjacent_ones = []
        if x < self.x_size - 1:
            # There is a right adjacent value
            adjacent_ones.append((y, x + 1))
        if y < self.y_size - 1:
            # There is a bottom adjacent value
            adjacent_ones.append((y + 1, x))
        if x > 0:
            # There is a left adjacent value
            adjacent_ones.append((y, x - 1))
        if y > 0:
            # There is a top adjacent value
            adjacent_ones.append((y - 1, x))
        return adjacent_ones

    def best_path(self) -> int:
        q = []
        heapq.heappush(q, (0, 0, 0))
        while True:
            r, y, x = heapq.heappop(q)

            # End of path?
            if x == self.x_size - 1 and y == self.y_size - 1:
                return r

            # Check all adjacent paths
            for y1, x1 in self.find_adjacent_ones(y, x):
                # Reckon new total risk
                new_r = r + self.risks[y1][x1]
                if self.best_paths[y1][x1] is None or new_r < self.best_paths[y1][x1]:
                    self.best_paths[y1][x1] = new_r
                    heapq.heappush(q, (new_r, y1, x1))
