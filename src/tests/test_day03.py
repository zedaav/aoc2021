from tests.utils import AOC2021Tester


class TestDay3(AOC2021Tester):
    def test_day3_1_sample(self):
        self.check_method(3.1, "day03-sample.txt", "Result: 198.")

    def test_day3_1_real(self):
        self.check_method(3.1, "day03-real.txt", "Result: 1071734.")

    def test_day3_2_sample(self):
        self.check_method(3.2, "day03-sample.txt", "Result: 230.")

    def test_day3_2_real(self):
        self.check_method(3.2, "day03-real.txt", "Result: 6124992.")
