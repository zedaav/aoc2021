import importlib
import logging
from argparse import ArgumentParser
from pathlib import Path
from typing import List

import coloredlogs


class AOC2021Resolver:
    def __init__(self, argv: List[str] = None):
        # Parse args
        parser = ArgumentParser(description="Solutions for AoC 2021")
        parser.add_argument("-i", "--input", type=Path, help="Path to input file", required=True)
        parser.add_argument("-d", "--day", type=float, help="Puzzle day (e.g. 1.1)", required=True)
        parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Verbose logs")
        self.args = parser.parse_args(argv)

    def process(self):
        # Prepare logs
        coloredlogs.install(level=logging.DEBUG if self.args.verbose else logging.INFO, fmt="%(levelname)s - %(message)s", reconfigure=True)

        # Read lines
        with self.args.input.open() as f:
            lines = [line.strip("\r\n ") for line in f.readlines()]

        # Delegate
        day_module = f"aoc2021.day{int(self.args.day):02}_{str(self.args.day)[-1:]}"
        logging.debug(f"Processing puzzle for {day_module}")
        module = importlib.import_module(day_module)
        module.process(lines)


def main():  # pragma: no cover
    AOC2021Resolver().process()
