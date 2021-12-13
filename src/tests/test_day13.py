from tests.utils import AOC2021Tester


class TestDay13(AOC2021Tester):
    def test_day13_1_sample(self):
        self.check_method(13.1, "day13-sample.txt", "Result: 17.")

    def test_day13_1_real(self):
        self.check_method(13.1, "day13-real.txt", "Result: 810.")

    def test_day13_2_sample(self):
        self.check_method(13.2, "day13-sample.txt", "Result: 16.")

    def test_day13_2_real(self):
        self.check_method(13.2, "day13-real.txt", "Result: 103.")
