import logging
import re
from typing import Dict, List

TEMPLATE_PATTERN = re.compile("^([A-Z]+)$")
INSTRUCTION_PATTERN = re.compile("([A-Z])([A-Z]) -> ([A-Z])")


class PolymerProcessor:
    def __init__(self, lines: List[str]):
        # Iterate on lines
        self.instructions = {}
        for line in lines:
            m = INSTRUCTION_PATTERN.match(line)
            if m is not None:
                self.instructions[m.group(1) + m.group(2)] = (m.group(3), [m.group(1) + m.group(3), m.group(3) + m.group(2)])
            else:
                m = TEMPLATE_PATTERN.match(line)
                if m is not None:
                    template = m.group(1)

        # Build initial pairs
        self.pairs = {}
        for i in range(len(template) - 1):
            pair = template[i : i + 2]
            self.add_elem(pair, self.pairs)

        # Count elements
        self.counts = {}
        for elem in template:
            self.add_elem(elem, self.counts)

        logging.debug(f"Start template/pairs: {template} / {self.pairs}; instructions: {len(self.instructions)}")
        logging.debug(f"Start count: {self.counts}")

    def add_elem(self, pair: str, impacted_map: Dict[str, int], count: int = 1):
        if pair not in impacted_map:
            impacted_map[pair] = 0
        impacted_map[pair] += count

    def process(self, steps: int):
        # Iterate on steps
        for _step in range(steps):
            # Iterate on instructions
            pairs_to_merge = {}
            pairs_to_remove = []
            for pair_to_search, (elem_to_add, pairs_to_add) in self.instructions.items():
                # Know pair in current template?
                if pair_to_search in self.pairs:
                    pairs_count = self.pairs[pair_to_search]
                    # Add resulting pairs
                    for pair_to_add in pairs_to_add:
                        self.add_elem(pair_to_add, pairs_to_merge, pairs_count)

                    # Remove found pair
                    pairs_to_remove.append(pair_to_search)

                    # Count new elements
                    self.add_elem(elem_to_add, self.counts, pairs_count)

            # Remove all found pairs (all split in to 2 new pairs)
            for p in pairs_to_remove:
                del self.pairs[p]

            # Add all new pairs
            for p, c in pairs_to_merge.items():
                self.add_elem(p, self.pairs, c)

            logging.debug(f"Pairs after step {_step+1}: {self.pairs}")

    def count(self):
        # Substract max count - min count
        return max(self.counts.values()) - min(self.counts.values())
