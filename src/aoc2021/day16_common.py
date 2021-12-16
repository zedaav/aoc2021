import logging

from bitarray import bitarray
from bitarray.util import hex2ba


class Packet:
    def __init__(self, ba: bitarray):
        # Read header
        self.ba = ba
        self.consumed_bits = 0
        self.version = self.read_int(3)
        self.type = self.read_int(3)
        self.value = None
        self.sub_packets = []
        self.op_matrix = {
            0: self.op_sum,
            1: self.op_product,
            2: self.op_min,
            3: self.op_max,
            4: self.op_value,
            5: self.op_greater,
            6: self.op_lesser,
            7: self.op_equals,
        }
        prefix = f"New package (v:{self.version} t:{self.type}) --> "

        # Is a literal value?
        if self.type == 4:
            self.value = bitarray()
            go_on = 1
            while go_on:
                # Continue?
                go_on = self.read_int(1)

                # Append next for bits to value
                self.value += self.read_bits(4)
            logging.debug(prefix + f"literal (value: {self.value})")
        else:
            # Operator packet
            # Check length type
            len_type = self.read_int(1)
            prefix += f"operator [l:{len_type}"
            if len_type:
                # Number of sub-packets, encoded on 11 bits
                sub_packets_count = self.read_int(11)
                prefix += f":{sub_packets_count}]"

                # Iterate on count
                logging.debug(prefix + f" ({sub_packets_count} sub-packets)")
                for _index in range(sub_packets_count):
                    new_packet = Packet(self.ba)
                    self.consumed_bits += new_packet.consumed_bits
                    self.sub_packets.append(new_packet)
            else:
                # Total length of sub-packets
                sub_packets_len = self.read_int(15)
                prefix += f":{sub_packets_len}]"
                consumed_len = 0
                logging.debug(prefix + f" (sub-packets on {sub_packets_len} bits)")
                while consumed_len < sub_packets_len:
                    new_packet = Packet(self.ba)
                    self.consumed_bits += new_packet.consumed_bits
                    consumed_len += new_packet.consumed_bits
                    self.sub_packets.append(new_packet)

    def read_bits(self, bits: int) -> bitarray:
        self.consumed_bits += bits
        out = self.ba[0:bits]
        del self.ba[0:bits]
        return out

    def read_int(self, bits: int = None, ba: bitarray = None) -> int:
        return int("0b" + (self.read_bits(bits) if ba is None else ba).to01(), base=2)

    def reckon(self) -> int:
        # Reckoned value depend on the package type
        return self.op_matrix[self.type]()

    def op_sum(self) -> int:
        return sum(p.reckon() for p in self.sub_packets)

    def op_product(self) -> int:
        out = 1
        for p in self.sub_packets:
            out *= p.reckon()
        return out

    def op_min(self) -> int:
        return min(p.reckon() for p in self.sub_packets)

    def op_max(self) -> int:
        return max(p.reckon() for p in self.sub_packets)

    def op_value(self) -> int:
        return self.read_int(ba=self.value)

    def op_greater(self) -> int:
        return 1 if self.sub_packets[0].reckon() > self.sub_packets[1].reckon() else 0

    def op_lesser(self) -> int:
        return 1 if self.sub_packets[0].reckon() < self.sub_packets[1].reckon() else 0

    def op_equals(self) -> int:
        return 1 if self.sub_packets[0].reckon() == self.sub_packets[1].reckon() else 0


class PacketsProcessor:
    def __init__(self, str_input: str):
        # Build bit array
        ba = hex2ba(str_input)
        logging.debug(f"Bits array: {ba}")
        self.root_packet = Packet(ba)
