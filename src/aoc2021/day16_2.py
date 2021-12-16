import logging
from typing import List

from aoc2021.day16_common import PacketsProcessor


def process(inputs: List[str]):
    # Process packets
    p = PacketsProcessor(inputs[0])

    # Reckon top packet value
    logging.info(f"Result: {p.root_packet.reckon()}.")
