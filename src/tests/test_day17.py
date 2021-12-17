from tests.utils import AOC2021Tester


class TestDay17(AOC2021Tester):
    def test_day17_1_sample(self):
        self.check_method(17.1, "day17-sample.txt", "Result: 45.")

    def test_day17_1_real(self):
        self.check_method(17.1, "day17-real.txt", "Result: 2850.")

    def test_day17_2_sample(self):
        self.check_method(17.2, "day17-sample.txt", "Result: 112.")

    def test_day17_2_real(self):
        self.check_method(17.2, "day17-real.txt", "Result: 1117.")
