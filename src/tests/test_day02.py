from aoc2021.day02_1 import day02_1
from aoc2021.day02_2 import day02_2
from tests.utils import AOC2021Tester


class TestDay2(AOC2021Tester):
    def test_day2_1_sample(self, capsys):
        self.check_method(day02_1, [(AOC2021Tester.INPUTS / "day02-sample.txt").as_posix()], "Result: 150.", capsys)

    def test_day2_1_real(self, capsys):
        self.check_method(day02_1, [(AOC2021Tester.INPUTS / "day02-real.txt").as_posix()], "Result: 1693300.", capsys)

    def test_day2_2_sample(self, capsys):
        self.check_method(day02_2, [(AOC2021Tester.INPUTS / "day02-sample.txt").as_posix()], "Result: 900.", capsys)

    def test_day2_2_real(self, capsys):
        self.check_method(day02_2, [(AOC2021Tester.INPUTS / "day02-real.txt").as_posix()], "Result: 1857958050.", capsys)
