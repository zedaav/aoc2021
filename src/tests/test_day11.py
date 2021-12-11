from tests.utils import AOC2021Tester


class TestDay11(AOC2021Tester):
    def test_day11_1_sample(self):
        self.check_method(11.1, "day11-sample.txt", "Result: 1656.")

    def test_day11_1_real(self):
        self.check_method(11.1, "day11-real.txt", "Result: 1681.")

    def test_day11_2_sample(self):
        self.check_method(11.2, "day11-sample.txt", "Result: 195.")

    def test_day11_2_real(self):
        self.check_method(11.2, "day11-real.txt", "Result: 276.")
