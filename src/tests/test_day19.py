from tests.utils import AOC2021Tester


class TestDay19(AOC2021Tester):
    def test_day19_1_sample(self):
        self.check_method(19.1, "day19-sample.txt", "Result: 79.")

    def test_day19_1_real(self):
        self.check_method(19.1, "day19-real.txt", "Result: 442.")

    def test_day19_2_sample(self):
        self.check_method(19.2, "day19-sample.txt", "Result: 3621.")

    def test_day19_2_real(self):
        self.check_method(19.2, "day19-real.txt", "Result: 11079.")
