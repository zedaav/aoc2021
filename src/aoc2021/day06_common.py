import logging
from typing import List

# Created fishes count per remaining days
RECKON_CACHE = {}


def new_created_fishes(remaining_days: int, initial_count: int = None) -> int:
    if initial_count is None and remaining_days in RECKON_CACHE:
        # Use cache
        return RECKON_CACHE[remaining_days]

    # Really remaining days count
    real_remaining = remaining_days - (8 if initial_count is None else initial_count) - 1
    if real_remaining < 0:
        # Not enough time to create a new fish
        return 0
    else:
        new = 1 + int(real_remaining / 7)
    out = new
    for i in range(new):
        out += new_created_fishes(real_remaining - (7 * i))

    # Store in cache
    if initial_count is None:
        RECKON_CACHE[remaining_days] = out
    return out


def process_fishes(fishes: List[int], days: int) -> int:
    # Iterate on fishes
    by_initial_index = {}
    for initial in fishes:
        # Count one more fish for this initial state
        if initial not in by_initial_index:
            by_initial_index[initial] = 0
        by_initial_index[initial] += 1
    logging.debug(f"Count of initial values: {by_initial_index}")

    # Iterate on initial indexes to reckon final count
    final_count = {}
    for first_init_count in by_initial_index.keys():
        # Start with one fish (the initial one), and add all descendents of this one
        final_count[first_init_count] = 1 + new_created_fishes(days, first_init_count)

    logging.debug(f"Count by initial values after {days} days: {final_count}")

    # Big sum
    return sum([final_count[x] * by_initial_index[x] for x in final_count.keys()])


# Easy solution, not usable with large numbers
def process_fishes_simple(fishes: List[int], days: int) -> int:  # pragma: no cover
    # Iterate on days
    for day in range(days):
        logging.debug(f"Day {day+1}: {len(fishes)}")
        initial_len = len(fishes)
        for index in range(initial_len):
            if fishes[index] == 0:
                # New fish!
                fishes[index] = 6
                fishes.append(8)
            else:
                fishes[index] -= 1
    return len(fishes)
