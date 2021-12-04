from tests.utils import AOC2021Tester


class TestDay4(AOC2021Tester):
    def test_day4_1_sample(self):
        self.check_method(4.1, "day04-sample.txt", "Result: 4512.")

    def test_day4_1_sample2(self):
        self.check_method(4.1, "day04-sample2.txt", "Result: 242.")

    def test_day4_1_real(self):
        self.check_method(4.1, "day04-real.txt", "Result: 50008.")

    def test_day4_2_sample(self):
        self.check_method(4.2, "day04-sample.txt", "Result: 1924.")

    def test_day4_2_sample2(self):
        self.check_method(4.2, "day04-sample2.txt", "Result: 3648.")

    def test_day4_2_real(self):
        self.check_method(4.2, "day04-real.txt", "Result: 17408.")
