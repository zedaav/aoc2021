from tests.utils import AOC2021Tester


class TestDay10(AOC2021Tester):
    def test_day10_1_sample(self):
        self.check_method(10.1, "day10-sample.txt", "Result: 26397.")

    def test_day10_1_real(self):
        self.check_method(10.1, "day10-real.txt", "Result: 343863.")

    def test_day10_2_sample(self):
        self.check_method(10.2, "day10-sample.txt", "Result: 288957.")

    def test_day10_2_real(self):
        self.check_method(10.2, "day10-real.txt", "Result: 2924734236.")
