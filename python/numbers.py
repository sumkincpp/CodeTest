print(0xFF)  # => 255
print(0o100)  # => 64


a = int('01110101', 2)  # => 117
print(a)

print(1 << 7)  # => 127
print(127 >> 2)  # => 127

print((127).bit_length())  # => 7

print(f"{42:b}")  # Print 42 in binary
print(f"{42:032b}")  # Print 42 in binary on 32 zero-padded digits


def xor(a, b):
    return (a and not b) or (not a and b)


def xor2(a, b):
    return (a + b) % 2


from struct import pack, unpack

pack(">I", 1969)  # Big-endian unsigned int b'\x00\x00\x07\xb1'

unpack("<I", b"\x00\x00\x07\xb1")  # Little-endian unsigned int (2970025984,)


from socket import htons, htonl, ntohs, ntohl
htons(1969)  # Host to network (short int) 45319
htonl(1969)  # Host to network (long int) 2970025984
ntohs(45319)  # Network to host (short int) 1969
ntohl(2970025984)  # Network to host (long int) 1969


def get_bit(value, bit_index):
    return value & (1 << bit_index)


def set_bit(value, bit_index):
    return value | (1 << bit_index)


def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)


def toggle_bit(value, bit_index):
    return value ^ (1 << bit_index)
