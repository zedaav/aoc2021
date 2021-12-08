from tests.utils import AOC2021Tester


class TestDay8(AOC2021Tester):
    def test_day8_1_sample(self):
        self.check_method(8.1, "day08-sample.txt", "Result: 26.")

    def test_day8_1_sample2(self):
        self.check_method(8.1, "day08-simple-sample.txt", "Result: 0.")

    def test_day8_1_real(self):
        self.check_method(8.1, "day08-real.txt", "Result: 369.")

    def test_day8_2_sample(self):
        self.check_method(8.2, "day08-sample.txt", "Result: 61229.")

    def test_day8_2_sample2(self):
        self.check_method(8.2, "day08-simple-sample.txt", "Result: 5353.")

    def test_day8_2_real(self):
        self.check_method(8.2, "day08-real.txt", "Result: 1031553.")
