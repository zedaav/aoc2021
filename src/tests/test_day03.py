from aoc2021.day03_1 import day03_1
from aoc2021.day03_2 import day03_2
from tests.utils import AOC2021Tester


class TestDay3(AOC2021Tester):
    def test_day3_1_sample(self, capsys):
        self.check_method(day03_1, [(AOC2021Tester.INPUTS / "day03-sample.txt").as_posix()], "Result: 198.", capsys)

    def test_day3_1_real(self, capsys):
        self.check_method(day03_1, [(AOC2021Tester.INPUTS / "day03-real.txt").as_posix()], "Result: 1071734.", capsys)

    def test_day3_2_sample(self, capsys):
        self.check_method(day03_2, [(AOC2021Tester.INPUTS / "day03-sample.txt").as_posix()], "Result: 230.", capsys)

    def test_day3_2_real(self, capsys):
        self.check_method(day03_2, [(AOC2021Tester.INPUTS / "day03-real.txt").as_posix()], "Result: 6124992.", capsys)
