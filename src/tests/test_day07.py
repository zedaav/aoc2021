from tests.utils import AOC2021Tester


class TestDay7(AOC2021Tester):
    def test_day7_1_sample(self):
        self.check_method(7.1, "day07-sample.txt", "Result: 37.")

    def test_day7_1_real(self):
        self.check_method(7.1, "day07-real.txt", "Result: 341534.")

    def test_day7_2_sample(self):
        self.check_method(7.2, "day07-sample.txt", "Result: 168.")

    def test_day7_2_real(self):
        self.check_method(7.2, "day07-real.txt", "Result: 93397632.")
