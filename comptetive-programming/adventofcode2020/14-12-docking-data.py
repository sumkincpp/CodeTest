#!/usr/bin/env python
#
# Your lucky number has been reconnected.
#
import re
import sys
import math

from functools import reduce
import operator
from typing import Dict

from collections import defaultdict
import pytest


##################################################################################
# Useful functions
##################################################################################


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


# pls
def yield_binary(num):
    n = num
    while n > 0:
        yield n % 2
        n //= 2


@pytest.mark.parametrize(
    "n,e",
    [
        (8, [0, 0, 0, 1]),
    ],
)
def test_yield_binary(n, e):
    assert list(yield_binary(n)) == e


def expand_binary_pattern(n: str):
    """
    Expands binary string pattern and yields all possible variants

    Example:
        X -> 0 and 1
        1X -> 10 and 11 in binary -> 3 and 4

    :param n: pattern with 0, 1, X, example: 10101X0XX
    :type n: str
    :yield: number variant
    """

    numbers = [n]

    while numbers:
        current = numbers.pop()

        print(current)
        X_index = current.find("X")

        if X_index == -1:
            yield int(current, 2)
        else:
            numbers.append(current.replace("X", "1", 1))
            numbers.append(current.replace("X", "0", 1))


@pytest.mark.parametrize(
    "n,e",
    [
        ("1000X", [16, 17]),
        ("1X", [3, 4]),
        ("X", [0, 1]),
        ("XX", [0, 1, 2, 3]),
    ],
)
def test_expand_binary_pattern(n, e):
    assert list(expand_binary_pattern(n)) == e


##################################################################################


def docking_data_part1(iterator):

    mask = None

    result_value = 0

    addresses = defaultdict(int)

    for line in iterator:
        line = line.strip()

        match_mask = re.match(r'mask = ([0-1X]+)$', line)

        if match_mask:
            mask = match_mask.group(1)
            result_value = 0
            continue

        match_mem = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)

        if not match_mem:
            print(line)
            raise ValueError("That's strange!")

        address, value = match_mem.groups()

        # print(f"address={address} value={value}")

        mask_len = len(mask)

        result_value = int(mask.replace("X", "0"), 2)

        for i, b1 in enumerate(yield_binary(int(value))):
            # mask bit
            b2 = mask[mask_len - i - 1]

            if b2 == 'X':
                bit = b1
            else:
                bit = int(b2)

            # print("{} {} {}".format(b1, b2, bit))

            if bit == 1:
                result_value |= 1 << i

        # print(result_value)
        addresses[address] = result_value

    return sum(addresses.values())


##################################################################################


def docking_data_part2(iterator):

    mask = None

    addresses = defaultdict(int)

    for line in iterator:
        line = line.strip()

        match_mask = re.match(r'mask = ([0-1X]+)$', line)

        if match_mask:
            mask = match_mask.group(1)
            result_value = 0
            continue

        match_mem = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)

        if not match_mem:
            print(line)
            raise ValueError("That's strange!")

        address, value = match_mem.groups()
        mask_len = len(mask)

        result = list(mask)

        for i, b1 in enumerate(yield_binary(int(address))):
            # mask bit
            b2 = mask[mask_len - i - 1]

            if b2 == 'X':
                bit = 'X'
            elif b2 == '0':
                bit = str(b1)
            elif b2 == '1':
                bit = "1"
            else:
                raise ValueError("oops!")

            # print("{} {} {} {}".format(i, b1, b2, bit))

            result[mask_len - i - 1] = bit

        res_str = "".join(result)

        for a in expand_binary_pattern(res_str):
            addresses[a] = int(value)

    return sum(addresses.values())


BASE_TEST = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0",
]

BASE_TEST_PART1 = [
    (BASE_TEST, 165),
]


@pytest.mark.parametrize('lines,expected', BASE_TEST_PART1)
def test_docking_data_part1(lines, expected):
    assert docking_data_part1(lines) == expected


BASE_TEST2 = [
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1",
]

BASE_TEST_PART2 = [
    (BASE_TEST2, 208),
]


@pytest.mark.parametrize('lines,expected', BASE_TEST_PART2)
def test_docking_data_part2(lines, expected):
    assert docking_data_part2(lines) == expected


if __name__ == "__main__":
    # num = calculate_deparature_time_part1(sys.stdin)
    num = docking_data_part2(sys.stdin)
    print("{0}".format(num))
