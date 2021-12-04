import logging
from typing import List


def process(lines: List[str]):
    # Process diagnostics
    diagnostics = [int("0b" + line, base=0) for line in lines]

    # Get prepared
    sample_size = len(lines[0])
    logging.debug(f"sample size: {sample_size}")

    # Reckon oxygen and CO2
    oxygen_diags = list(diagnostics)
    co2_diags = list(diagnostics)
    for i in range(sample_size - 1, -1, -1):
        for remaining_diags in [oxygen_diags, co2_diags]:
            # Still something to filter?
            if len(remaining_diags) > 1:
                ones_count = sum([(diagnostic >> i) & 1 for diagnostic in remaining_diags])
                if ones_count >= len(remaining_diags) / 2:
                    most = 1
                    least = 0
                else:
                    most = 0
                    least = 1

                # Filter list down
                if remaining_diags == oxygen_diags:
                    # Filter for oxygen: keep most common bit
                    oxygen_diags = list(filter(lambda diag: ((diag >> i) & 1) == most, oxygen_diags))
                else:
                    # Filter for co2: keep least common bit
                    co2_diags = list(filter(lambda diag: ((diag >> i) & 1) == least, co2_diags))

    # There shall be one remaining value in both lists
    assert len(oxygen_diags) == 1
    oxygen = oxygen_diags[0]
    assert len(co2_diags) == 1
    co2 = co2_diags[0]

    # Final life support
    logging.debug(f"oxygen: {oxygen} ({bin(oxygen)})")
    logging.debug(f"co2: {co2} ({bin(co2)})")
    logging.info(f"Result: {oxygen * co2}.")
