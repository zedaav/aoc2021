from tests.utils import AOC2021Tester


class TestDay14(AOC2021Tester):
    def test_day14_1_sample(self):
        self.check_method(14.1, "day14-sample.txt", "Result: 1588.")

    def test_day14_1_real(self):
        self.check_method(14.1, "day14-real.txt", "Result: 2345.")

    def test_day14_2_sample(self):
        self.check_method(14.2, "day14-sample.txt", "Result: 2188189693529.")

    def test_day14_2_real(self):
        self.check_method(14.2, "day14-real.txt", "Result: 2432786807053.")
