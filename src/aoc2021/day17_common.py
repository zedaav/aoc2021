import logging
import re
from dataclasses import dataclass
from typing import List, Tuple

TARGET_PATTERN = re.compile("target area: x=([0-9]+)..([0-9]+), y=([-0-9]+)..([-0-9]+)")

INT_SERIES_CACHE = {}


def int_series(target: int) -> List[int]:
    if target not in INT_SERIES_CACHE:
        series = [target]
        for i in range(target - 1, 0, -1):
            series.append(series[-1] + i)
        INT_SERIES_CACHE[target] = series
    return INT_SERIES_CACHE[target]


@dataclass
class Target:
    left: int
    right: int
    bottom: int
    top: int

    def x_ok(self, x: int) -> bool:
        return x >= self.left and x <= self.right


class Trajectory:
    def __init__(self, target: Target, velocity: Tuple[int, int]) -> None:
        self.target = target
        self.v_x, self.v_y = velocity
        self.points = [(0, 0)]

        # Add points until we're in target (or beyond it)
        while not self.in_target and not self.beyond_target:
            # Add new point
            last_x, last_y = self.points[-1]
            self.points.append((last_x + self.v_x, last_y + self.v_y))

            # Update velocities
            self.v_x -= 1 if self.v_x > 0 else 0
            self.v_y -= 1

    @property
    def in_target(self) -> bool:
        x, y = self.points[-1]
        return self.target.x_ok(x) and self.compare_y(y, self.target.top) <= 0 and self.compare_y(y, self.target.bottom) >= 0

    @property
    def beyond_target(self) -> bool:
        x, y = self.points[-1]
        return x > self.target.right or self.compare_y(y, self.target.bottom) < 0

    def compare_y(self, y: int, edge: int) -> int:
        """
        > 0 if y higher than edge
        < 0 if y lower than edge
        = 0 if same
        """
        if y >= 0:
            return y - edge  # if edge >= 0, real comparison; if edge < 0, always >0
        else:
            if edge >= 0:  # pragma: no cover
                return y  # always <0
            else:
                return -edge - -y


class TargetProcessor:
    def __init__(self, target: str):
        # Parse target area
        m = TARGET_PATTERN.match(target)
        assert m is not None
        self.target = Target(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        logging.debug(f"Target: {self.target.left}x{self.target.right} on {self.target.top}x{self.target.bottom}")

    def trajectories(self) -> List[Trajectory]:
        # Find all x velocities that have a chance to fit in target
        x_candidates = []
        for x_try in range(1, self.target.right + 1):
            series = int_series(x_try)
            if any(self.target.x_ok(x) for x in series):
                x_candidates.append(x_try)
        logging.debug(f"All candidate x velocities: {x_candidates}")

        # Find all fitting trajectories
        out = []
        for y_try in range(self.target.bottom, abs(self.target.bottom)):
            for x_try in x_candidates:
                t = Trajectory(self.target, (x_try, y_try))
                if t.in_target:
                    # At least one fitting trajectory for this y
                    out.append(t)
                    logging.debug(f"New fitting trajectory: {x_try},{y_try}")
            y_try += 1
        return out
