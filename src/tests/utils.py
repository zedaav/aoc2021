import logging
from pathlib import Path
from typing import Callable, List

from pytest_multilog import TestHelper


class AOC2021Tester(TestHelper):
    INPUTS = Path(__file__).parent.parent.parent / "inputs"

    def check_method(self, method: Callable, input: List[str], expected: str, capsys):
        # Call method
        logging.debug(f"Calling method {method.__name__} with args: {input}")
        method(input)

        # Capture output
        captured = capsys.readouterr()
        logging.debug(f"Captured stdout:\n{captured.out}")
        logging.debug(f"Captured stdout:\n{captured.err}")

        # Verify expected out
        assert expected in captured.out
