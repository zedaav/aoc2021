import logging
import re
from functools import lru_cache
from typing import Dict, List, Tuple

SCANNER_HEADER = re.compile("--- scanner ([0-9]+) ---")
BEACON_POS = re.compile("([-0-9]+),([-0-9]+),([-0-9]+)")


def rotate_y(coords: Tuple[int, int, int]):
    x, y, z = coords
    return (z, y, -x)


def rotate_x(coords: Tuple[int, int, int]):
    x, y, z = coords
    return (x, z, -y)


def rotate_z(coords: Tuple[int, int, int]):
    x, y, z = coords
    return (-y, x, z)


# Reckon all positions combinations
ALL_COMBINATIONS = []
__current = (1, 2, 3)
for face_up in [rotate_x, rotate_x, rotate_z, rotate_x, rotate_x, rotate_z]:
    for turn_left in [rotate_y] * 4:
        ALL_COMBINATIONS.append(__current)
        __current = turn_left(__current)
    __current = face_up(__current)


@lru_cache(maxsize=None)
def get_beacon_coord(beacon: Tuple[int, int, int], p: int) -> int:
    return beacon[abs(p) - 1] * (p // abs(p))


@lru_cache(maxsize=None)
def get_rotated_beacons(
    beacons: Tuple[Tuple[int, int, int]], position: Tuple[int, int, int], relative_to: Tuple[int, int, int], rotate_relative: bool
) -> Tuple[Tuple[int, int, int]]:
    """
    Returns a copy of beacons, with following modifications:
    * beacons: beacons to be reordered
    * position: rotation to be applied
    * relative_to: a tuple of offsets to be directly added
    * sign: sign to use on addition
    * rotate_relative: True if relative needs to be rotated before being added
    """
    # Iterate on beacons
    out = []
    for beacon in beacons:
        # Rotate it according to required position, and get coordinates relative to required beacon
        out.append(
            tuple(
                map(
                    lambda i: get_beacon_coord(beacon, position[i])
                    + (-1 if rotate_relative else 1) * get_beacon_coord(relative_to, position[i] if rotate_relative else i + 1),
                    range(len(position)),
                )
            )
        )
    return tuple(out)


class Scanner:
    def __init__(self, sid: int, beacons: List[Tuple[int, int, int]], known_pos=False):
        self.sid = sid
        self.beacons = tuple(beacons)
        self.known_pos = known_pos
        self.coords = (0, 0, 0) if known_pos else None
        self._cached_rotated_beacons = {}
        logging.debug(f"New scanner {self.sid}")

    def update_coord(self, position: Tuple[int, int, int], coords: Tuple[int, int, int]):
        self.known_pos = True
        self.coords = coords

        # Update all beacons with repositioned scanner coordinates + position
        self.beacons = get_rotated_beacons(self.beacons, position, coords, False)
        self._cached_rotated_beacons = {}
        logging.debug(f"Scanner {self.sid} positions updated!")

    def find_common_beacons(self, other: object) -> bool:
        # Can be called only on a Scanner with up-to-date positions
        assert self.known_pos

        # Iterage on self beacons
        for self_reference in self.beacons:
            self_rotated_beacons = get_rotated_beacons(self.beacons, ALL_COMBINATIONS[0], self_reference, True)
            # Iterate on other beacons
            for other_reference in other.beacons:
                # Iterate on possible positions
                for position in ALL_COMBINATIONS:
                    # Verify beacons intersection
                    other_rotated_beacons = get_rotated_beacons(other.beacons, position, other_reference, True)
                    common_beacons = list(set(self_rotated_beacons) & set(other_rotated_beacons))
                    if len(common_beacons) >= 12 and (0, 0, 0) in common_beacons:
                        # Reckon other scanner position
                        other_rotated_reference = tuple(map(lambda p: get_beacon_coord(other_reference, p), position))
                        other_coord = (
                            self_reference[0] - other_rotated_reference[0],
                            self_reference[1] - other_rotated_reference[1],
                            self_reference[2] - other_rotated_reference[2],
                        )
                        other.update_coord(position, other_coord)
                        return True

        return False


def parse_scanners(scanners: List[str]) -> Dict[int, Scanner]:
    # Iterate on lines
    out = []
    current_sid = None
    current_beacons = []
    known_pos = True
    for line in scanners:
        m = SCANNER_HEADER.match(line)
        if m is not None:
            # End of previous scanner
            if current_sid is not None:
                out.append(Scanner(current_sid, current_beacons, known_pos))
                known_pos = False

            # New scanner
            current_sid = int(m.group(1))
            current_beacons = []
        else:
            m = BEACON_POS.match(line)
            if m is not None:
                # New beacon
                current_beacons.append(tuple(map(lambda i: int(m.group(i)), range(1, 4))))

    # End of last scanner
    if current_sid is not None:  # pragma: no branch
        out.append(Scanner(current_sid, current_beacons))

    return out


def locate_all_beacons(scanners: List[Scanner]):
    # Find all common beacons
    known_stack = [0]
    known_stack_index = 0
    while known_stack_index < len(known_stack):
        current_known_scanner = scanners[known_stack[known_stack_index]]
        unknowns = list(filter(lambda i: i not in known_stack, range(len(scanners))))
        for unknown_candidate_index in unknowns:
            if current_known_scanner.find_common_beacons(scanners[unknown_candidate_index]):
                # New known scanner!
                known_stack.append(unknown_candidate_index)
        known_stack_index += 1
