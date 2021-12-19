import json
from copy import deepcopy
from typing import List, Tuple


class SnailFishNumber:
    def __init__(self, from_list: list):
        # Init from list
        assert len(from_list) == 2
        self.own_list = deepcopy(from_list)

    def __repr__(self) -> str:
        return f"{self.own_list}"

    def __add__(self, other: object) -> object:
        return SnailFishNumber([self.own_list, other.own_list])

    def reduce(self):
        # Iterate while something was reduced
        while self._explode() or self._split():
            pass

    def _explode(self) -> bool:
        # Iterate on all numbers
        all_nb = self.all_numbers()
        nb_count = len(all_nb)
        for i in range(nb_count):
            pos, nb = all_nb[i]
            next_pos, next_nb = all_nb[i + 1] if i < nb_count - 1 else (None, None)

            # Test for explode:
            # * at least 4 nested levels
            # * not the last number
            # * following number is same pair sibling
            if len(pos) > 4 and (next_pos is not None) and (pos[:-1] == next_pos[:-1]) and (len(pos) == len(next_pos)) and (pos[-1] == 0 and next_pos[-1] == 1):
                # Explode!
                # --> left
                if i > 0:
                    self.set_item(all_nb[i - 1][0], nb, replace=False)
                # --> right
                if i < nb_count - 2:
                    self.set_item(all_nb[i + 2][0], next_nb, replace=False)
                # --> replace by 0
                self.set_item(pos[:-1], 0, replace=True)
                # --> stop here
                return True
        return False

    def _split(self) -> bool:
        # Iterate on all numbers
        all_nb = self.all_numbers()
        nb_count = len(all_nb)
        for i in range(nb_count):
            pos, nb = all_nb[i]

            # Test for split
            if nb >= 10:
                self.set_item(pos, [int(nb / 2), int(nb / 2) + nb % 2], replace=True)
                return True
        return False

    def set_item(self, pos: List[int], value, replace: bool):
        item = self.own_list
        for p in pos[:-1]:
            item = item[p]
        if replace:
            # Replace
            item[pos[-1]] = value
        else:
            # Add
            item[pos[-1]] += value

    def all_numbers(self, item: list = None, pos: List[int] = None) -> List[Tuple[List[int], int]]:
        item = self.own_list if item is None else item
        pos = [] if pos is None else pos
        out = []
        for i in range(2):
            if isinstance(item[i], int):
                # New int
                out.append((pos + [i], item[i]))
            else:
                # Browse down the list elements
                out.extend(self.all_numbers(item[i], pos + [i]))
        return out

    def magnitude(self, item: list = None) -> int:
        item = self.own_list if item is None else item
        out = 0
        for i in range(2):
            out += (3 - i) * (item[i] if isinstance(item[i], int) else self.magnitude(item[i]))
        return out


def parse_numbers(numbers: List[str]) -> List[SnailFishNumber]:
    return [SnailFishNumber(json.loads(n)) for n in numbers]
