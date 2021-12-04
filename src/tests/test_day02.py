from tests.utils import AOC2021Tester


class TestDay2(AOC2021Tester):
    def test_day2_1_sample(self):
        self.check_method(2.1, "day02-sample.txt", "Result: 150.")

    def test_day2_1_real(self):
        self.check_method(2.1, "day02-real.txt", "Result: 1693300.")

    def test_day2_2_sample(self):
        self.check_method(2.2, "day02-sample.txt", "Result: 900.")

    def test_day2_2_real(self):
        self.check_method(2.2, "day02-real.txt", "Result: 1857958050.")
