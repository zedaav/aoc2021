from tests.utils import AOC2021Tester


class TestDay20(AOC2021Tester):
    def test_day20_1_sample(self):
        self.check_method(20.1, "day20-sample.txt", "Result: 35.")

    def test_day20_1_real(self):
        self.check_method(20.1, "day20-real.txt", "Result: 5339.")

    def test_day20_2_sample(self):
        self.check_method(20.2, "day20-sample.txt", "Result: 3351.")

    def test_day20_2_real(self):
        self.check_method(20.2, "day20-real.txt", "Result: 18395.")
