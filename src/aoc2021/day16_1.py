import logging
from typing import List

from aoc2021.day16_common import Packet, PacketsProcessor


def process(inputs: List[str]):
    # Process packets
    p = PacketsProcessor(inputs[0])

    # Sum versions
    def sum_v(packets: List[Packet]) -> int:
        return sum(p.version + sum_v(p.sub_packets) for p in packets)

    logging.info(f"Result: {sum_v([p.root_packet])}.")
