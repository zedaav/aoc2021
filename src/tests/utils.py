import logging
from pathlib import Path

from pytest_multilog import TestHelper

from aoc2021.__main__ import AOC2021Resolver


class AOC2021Tester(TestHelper):
    INPUTS = Path(__file__).parent.parent.parent / "inputs"

    def check_method(self, day: float, input: str, expected: str):
        # Call method
        logging.debug(f"Calling puzzle day {day} with input {input}")
        AOC2021Resolver(["-d", str(day), "-i", (AOC2021Tester.INPUTS / input).as_posix()]).process()

        # Verify expected out
        self.check_logs(expected)
