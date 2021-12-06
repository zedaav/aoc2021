from tests.utils import AOC2021Tester


class TestDay6(AOC2021Tester):
    def test_day6_1_sample(self):
        self.check_method(6.1, "day06-sample.txt", "Result: 5934.")

    def test_day6_1_sample2(self):
        self.check_method(6.1, "day06-sample0.txt", "Result: 1154.")

    def test_day6_1_real(self):
        self.check_method(6.1, "day06-real.txt", "Result: 388419.")

    def test_day6_2_sample(self):
        self.check_method(6.2, "day06-sample.txt", "Result: 26984457539.")

    def test_day6_2_sample2(self):
        self.check_method(6.2, "day06-sample0.txt", "Result: 5217223242.")

    def test_day6_2_real(self):
        self.check_method(6.2, "day06-real.txt", "Result: 1740449478328.")
