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


def yield_x_binary(n):
    """
    Simple and greedy X expansion
    """
    numbers = [n]

    new_numbers = []

    while numbers:
        current = numbers[0]
        X_index = current.find("X")

        if X_index == -1:
            for n in numbers:
                yield int(n, 2)
            return

        new_numbers = []
        for n in numbers:
            new_numbers.append(n.replace("X", "1", 1))
            new_numbers.append(n.replace("X", "0", 1))

        numbers = new_numbers


@pytest.mark.parametrize(
    "n,e",
    [
        ("X", [1, 0]),
        ("XX", [3, 2, 1, 0]),
    ],
)
def test_yield_x_binary(n, e):
    assert list(yield_x_binary(n)) == e


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

        for a in yield_x_binary(res_str):
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
