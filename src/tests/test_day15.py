from tests.utils import AOC2021Tester


class TestDay15(AOC2021Tester):
    def test_day15_1_sample(self):
        self.check_method(15.1, "day15-sample.txt", "Result: 40.")

    def test_day15_1_real(self):
        self.check_method(15.1, "day15-real.txt", "Result: 685.")

    def test_day15_2_sample(self):
        self.check_method(15.2, "day15-sample.txt", "Result: 315.")

    def test_day15_2_real(self):
        self.check_method(15.2, "day15-real.txt", "Result: 2995.")
