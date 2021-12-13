from tests.utils import AOC2021Tester


class TestDay12(AOC2021Tester):
    def test_day12_1_sample(self):
        self.check_method(12.1, "day12-sample1.txt", "Result: 10.")

    def test_day12_1_real(self):
        self.check_method(12.1, "day12-real.txt", "Result: 4495.")

    def test_day12_2_sample(self):
        self.check_method(12.2, "day12-sample1.txt", "Result: 36.")

    def test_day12_2_real(self):
        self.check_method(12.2, "day12-real.txt", "Result: 131254.")
