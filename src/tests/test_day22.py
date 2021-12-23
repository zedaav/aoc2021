from tests.utils import AOC2021Tester


class TestDay22(AOC2021Tester):
    def test_day22_1_sample(self):
        self.check_method(22.1, "day22-sample.txt", "Result: 474140.")

    def test_day22_1_real(self):
        self.check_method(22.1, "day22-real.txt", "Result: 524792.")

    def test_day22_2_sample(self):
        self.check_method(22.2, "day22-sample.txt", "Result: 2758514936282235.")

    def test_day22_2_real(self):
        self.check_method(22.2, "day22-real.txt", "Result: 1213461324555691.")
