import logging


def dump_table(table: list):
    # Simple table dump
    for line in table:
        logging.debug(f">> {line}")
