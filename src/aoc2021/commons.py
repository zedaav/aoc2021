import logging

INT_SUM_CACHE = {}


def int_sum(target: int) -> int:
    # Some maths: 1+2+3+4+5+....+N = (N*(N+1))/2
    if target not in INT_SUM_CACHE:
        INT_SUM_CACHE[target] = int((target * (target + 1)) / 2)
    return INT_SUM_CACHE[target]


def dump_table(table: list):
    # Simple table dump
    for line in table:
        logging.debug(f">> {line}")
