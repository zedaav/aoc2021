from typing import Dict, List, Tuple


def factorize_crabs(crabs: List[int]) -> Tuple[int, int, Dict[int, int]]:
    # Iterate first to factorize per initial pos + find min/max
    min_pos = max_pos = None
    crabs_map = {}
    for crab in crabs:
        if min_pos is None or crab < min_pos:
            min_pos = crab
        if max_pos is None or crab > max_pos:
            max_pos = crab
        if crab not in crabs_map:
            crabs_map[crab] = 0
        crabs_map[crab] += 1

    return min_pos, max_pos, crabs_map
