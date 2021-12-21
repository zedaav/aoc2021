import logging
import re
from abc import ABC, abstractmethod
from functools import lru_cache
from itertools import permutations
from typing import List, Tuple

import numpy

INIT_POS = re.compile("Player ([0-9]+) starting position: ([0-9]+)")


class Dice(ABC):
    @abstractmethod
    def roll(self) -> int:  # pragma: no cover
        pass


class DeterministicDice(Dice):
    def __init__(self, sides: int = 100):
        # All sums of 3 consecutive deterministic rolls
        self.all_rolls = numpy.concatenate((numpy.arange(1, sides + 1),) * 3).reshape((sides, 3)).sum(axis=1)
        self.pos = -1

    def roll(self) -> int:
        self.pos = (self.pos + 1) % len(self.all_rolls)
        return self.all_rolls[self.pos]


class DiracDice(Dice):
    def __init__(self, sides: int = 3):
        # All sums of all 3 consecutive possible rolls
        self.all_rolls = numpy.unique(numpy.array(list(set(permutations(numpy.concatenate((numpy.arange(1, sides + 1),) * sides)))))[:, 0:sides], axis=0).sum(
            axis=1
        )

    def roll(self) -> List[int]:
        return self.all_rolls


class Game:
    def __init__(self, players: List[Tuple[int, int]]):
        self.players = players
        assert len(players) == 2
        self.dirac_dice = DiracDice()
        self.deter_dice = DeterministicDice()

    def score(self, pid: int) -> int:
        return self.players[pid][1]

    def update(self, pid: int, roll: int):
        pos, score = self.players[pid]
        pos = (pos + roll - 1) % 10 + 1
        score += pos
        self.players[pid] = (pos, score)

    @lru_cache(maxsize=None)
    def all_universes(self, target: int, pos1: int, pos2: int, score1: int, score2: int) -> List[int]:
        if score1 >= target:
            return [1, 0]  # pragma: no cover
        if score2 >= target:
            return [0, 1]

        res = [0, 0]
        for roll in self.dirac_dice.roll():
            new_pos = (pos1 + roll - 1) % 10 + 1
            new_score = score1 + new_pos
            sub_res = self.all_universes(target, pos2, new_pos, score2, new_score)
            res = [res[0] + sub_res[1], res[1] + sub_res[0]]
        return res

    def play_dirac(self, target: int) -> int:
        res = self.all_universes(target, self.players[0][0], self.players[1][0], 0, 0)
        logging.debug(f"Winning universes for Player 1: {res[0]}")
        logging.debug(f"Winning universes for Player 2: {res[1]}")
        return max(res)

    def play_deter(self, target: int) -> int:
        rolls = 0
        while True:
            pid = rolls % 2
            self.update(pid, self.deter_dice.roll())
            rolls += 1
            if self.score(pid) >= target:
                logging.info(f"Player {pid+1} wins after {rolls*3} rolls")
                looser = (pid + 1) % 2
                break

        return rolls * 3 * self.score(looser)


def parse_positions(lines: List[str]) -> Game:
    return Game(list(map(lambda m: (int(m.group(2)), 0), filter(lambda m: m is not None, map(lambda line: INIT_POS.match(line), lines)))))
