import logging
from typing import Dict, List

from aoc2021.day08_commons import parse_patterns

# Known patterns lengths
# 6 may be: 0, 6 or 9
# 5 may be, 2, 3 or 5
KNOWN_PATTERNS = {2: 1, 4: 4, 3: 7, 7: 8, 5: -1, 6: -1}


def build_digits_from_patterns(input_patterns: List[str]) -> Dict[str, int]:
    # Order patterns by length
    patterns_by_len = {k: list(filter(lambda x: len(x) == k, input_patterns)) for k in KNOWN_PATTERNS.keys()}
    logging.debug(f"{patterns_by_len}")

    # Build easy to guess pattern --> digit matching
    digits_from_patterns = {patterns_by_len[ln][0]: KNOWN_PATTERNS[ln] for ln in filter(lambda x: KNOWN_PATTERNS[x] >= 0, KNOWN_PATTERNS.keys())}

    # Guess for 5 length
    p1 = patterns_by_len[2][0]
    p4 = patterns_by_len[4][0]
    for candidate in patterns_by_len[5]:
        if all(seg in candidate for seg in p1):
            # All 1 segments in candidate --> 3
            digits_from_patterns[candidate] = 3
            p3 = candidate
        elif len(list(filter(lambda s: s in p4, candidate))) == 3:
            # 3 same segments than 4 --> 5
            digits_from_patterns[candidate] = 5
            p5 = candidate
        else:
            # Last chance --> 2
            digits_from_patterns[candidate] = 2

    # Guess for 6 length
    for candidate in patterns_by_len[6]:
        if all(seg in candidate for seg in p3):
            # All 3 segments in candidate --> 9
            digits_from_patterns[candidate] = 9
        elif all(seg in candidate for seg in p5):
            # All 5 segments in candidate --> 6
            digits_from_patterns[candidate] = 6
        else:
            # Last chance --> 0
            digits_from_patterns[candidate] = 0

    logging.debug(f"{digits_from_patterns}")
    return digits_from_patterns


def process(instructions: List[str]):
    # Build patterns
    patterns = parse_patterns(instructions)

    # Sum outputs
    numbers_sum = 0
    for input_patterns, outputs in patterns:
        # Build pattern --> digit matching
        digits_from_patterns = build_digits_from_patterns(input_patterns)

        # Found each 4 digit
        number = 0
        for index in range(len(outputs)):
            output = outputs[index]
            for p, digit in digits_from_patterns.items():  # pragma: no branch
                if len(p) == len(output) and all(d in p for d in outputs[index]):
                    number += digit * pow(10, 3 - index)
                    break
        logging.debug(f"{outputs} --> {number}")
        numbers_sum += number

    # Final sum
    logging.info(f"Result: {numbers_sum}.")
