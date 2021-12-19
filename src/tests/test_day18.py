from tests.utils import AOC2021Tester


class TestDay18(AOC2021Tester):
    def test_day18_1_sample(self):
        self.check_method(18.1, "day18-sample.txt", "Result: 4140.")

    def test_day18_1_real(self):
        self.check_method(18.1, "day18-real.txt", "Result: 4120.")

    def test_day18_2_sample(self):
        self.check_method(18.2, "day18-sample.txt", "Result: 3993.")

    def test_day18_2_real(self):
        self.check_method(18.2, "day18-real.txt", "Result: 4725.")
