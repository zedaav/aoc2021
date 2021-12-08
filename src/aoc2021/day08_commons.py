import logging
from typing import List, Tuple


def parse_patterns(instructions: List[str]) -> List[Tuple[List[str], List[str]]]:
    # Build patterns
    patterns = []
    for instruction in instructions:
        parts = instruction.split(" | ")
        assert len(parts) == 2
        new_tuple = tuple([part.split(" ") for part in parts])
        assert len(new_tuple[0]) == 10
        assert len(new_tuple[1]) == 4
        patterns.append(new_tuple)
    logging.debug(f"Loaded patterns: {len(patterns)}")
    return patterns
