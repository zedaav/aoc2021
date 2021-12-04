import logging
from typing import List


def process(lines: List[str]):
    # Process diagnostics
    diagnostics = [int("0b" + line, base=0) for line in lines]

    # Loop on diagnostics
    diag_count = len(diagnostics)
    sample_size = len(lines[0])
    logging.debug(f"sample size: {sample_size}")
    gamma_bits = {i: [] for i in range(sample_size)}
    for diagnostic in diagnostics:
        for i in range(sample_size):
            bit = (diagnostic >> i) & 1
            gamma_bits[i].append(bit)

    # Reckon gamma
    gamma = 0
    for i in range(sample_size):
        ones_count = sum(gamma_bits[i])

        # Corner case: exactly same number of 1s & 0s
        assert ones_count != diag_count / 2, f"Don't known what to do at index {i}: {ones_count} 1s on {diag_count} diagnostics"

        gamma |= (1 if (ones_count > diag_count / 2) else 0) << i

    # Epsilon is gamma complement to 2
    epsilon = gamma ^ sum(1 << i for i in range(sample_size))

    # Final power consumption
    logging.debug(f"gamma: {gamma} ({bin(gamma)})")
    logging.debug(f"epsilon: {epsilon} ({bin(epsilon)})")
    logging.info(f"Result: {gamma * epsilon}.")
