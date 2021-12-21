from tests.utils import AOC2021Tester


class TestDay21(AOC2021Tester):
    def test_day21_1_sample(self):
        self.check_method(21.1, "day21-sample.txt", "Result: 739785.")

    def test_day21_1_real(self):
        self.check_method(21.1, "day21-real.txt", "Result: 802452.")

    def test_day21_2_sample(self):
        self.check_method(21.2, "day21-sample.txt", "Result: 444356092776315.")

    def test_day21_2_real(self):
        self.check_method(21.2, "day21-real.txt", "Result: 270005289024391.")
