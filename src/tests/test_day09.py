from tests.utils import AOC2021Tester


class TestDay9(AOC2021Tester):
    def test_day9_1_sample(self):
        self.check_method(9.1, "day09-sample.txt", "Result: 15.")

    def test_day9_1_real(self):
        self.check_method(9.1, "day09-real.txt", "Result: 489.")

    def test_day9_2_sample(self):
        self.check_method(9.2, "day09-sample.txt", "Result: 1134.")

    def test_day9_2_real(self):
        self.check_method(9.2, "day09-real.txt", "Result: 1056330.")
