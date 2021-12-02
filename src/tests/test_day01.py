from aoc2021.day01_1 import day01_1
from aoc2021.day01_2 import day01_2
from tests.utils import AOC2021Tester


class TestDay1(AOC2021Tester):
    def test_day1_1_sample(self, capsys):
        self.check_method(day01_1, [(AOC2021Tester.INPUTS / "day01-sample.txt").as_posix()], "Result: 7.", capsys)

    def test_day1_1_real(self, capsys):
        self.check_method(day01_1, [(AOC2021Tester.INPUTS / "day01-real.txt").as_posix()], "Result: 1298.", capsys)

    def test_day1_2_sample(self, capsys):
        self.check_method(day01_2, [(AOC2021Tester.INPUTS / "day01-sample.txt").as_posix()], "Result: 5.", capsys)

    def test_day1_2_real(self, capsys):
        self.check_method(day01_2, [(AOC2021Tester.INPUTS / "day01-real.txt").as_posix()], "Result: 1248.", capsys)
