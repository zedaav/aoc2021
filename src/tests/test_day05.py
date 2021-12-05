from tests.utils import AOC2021Tester


class TestDay5(AOC2021Tester):
    def test_day5_1_sample(self):
        self.check_method(5.1, "day05-sample.txt", "Result: 5.")

    def test_day5_1_real(self):
        self.check_method(5.1, "day05-real.txt", "Result: 7414.")

    def test_day5_2_sample(self):
        self.check_method(5.2, "day05-sample.txt", "Result: 12.")

    def test_day5_2_real(self):
        self.check_method(5.2, "day05-real.txt", "Result: 19676.")
