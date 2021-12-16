from tests.utils import AOC2021Tester


class TestDay16(AOC2021Tester):
    def test_day16_1_sample(self):
        self.check_method(16.1, "day16-sample.txt", "Result: 20.")

    def test_day16_1_real(self):
        self.check_method(16.1, "day16-real.txt", "Result: 963.")

    def test_day16_2_sample(self):
        self.check_method(16.2, "day16-sample.txt", "Result: 1.")

    def test_day16_2_real(self):
        self.check_method(16.2, "day16-real.txt", "Result: 1549026292886.")
