from tests.utils import AOC2021Tester


class TestDay1(AOC2021Tester):
    def test_day1_1_sample(self):
        self.check_method(1.1, "day01-sample.txt", "Result: 7.")

    def test_day1_1_real(self):
        self.check_method(1.1, "day01-real.txt", "Result: 1298.")

    def test_day1_2_sample(self):
        self.check_method(1.2, "day01-sample.txt", "Result: 5.")

    def test_day1_2_real(self):
        self.check_method(1.2, "day01-real.txt", "Result: 1248.")
