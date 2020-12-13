#!/usr/bin/env python
#
# Your lucky number has been disconnected.
#
import sys
import math

from functools import reduce
import operator
from typing import Dict

import pytest


##################################################################################
# Useful functions
##################################################################################


def lcm(a, b):
    # least common multiple
    return (a * b) // math.gcd(a, b)


def lcm_mult(*lst):
    curr = lst[0]

    for a in lst[1:]:
        curr = lcm(a, curr)

    return curr


def mod_inverse(a, m):
    """
    Naive mod inverse
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def chinese_remainder_theorem(numbers, remainders):
    """
    Chinese remainder theorem - calculates lowest number with remainder by modulo
    """

    assert len(numbers) == len(remainders)

    num_len = len(numbers)

    print(numbers)

    product = reduce(operator.mul, numbers, 1)

    m = [product // n for n in numbers]

    # m ^ -1
    invs = [mod_inverse(m[i], numbers[i]) for i in range(0, num_len)]

    print("product = {}".format(product))
    print("m = {}".format(m))
    print("invs = {}".format(invs))

    number_parts = [invs[i] * m[i] * remainders[i] for i in range(0, num_len)]
    number = sum(number_parts) % product

    print("number_parts = {}".format(number_parts))
    print("number = {}".format(number))

    return number


@pytest.mark.parametrize(
    "numbers,remainders,expected",
    [
        (
            [3, 4, 5],
            [2, 3, 1],
            11,
        ),
        (
            [7, 13],
            [0, -1],
            77,
        ),
    ],
)
def test_chinese_remainder_theorem(numbers, remainders, expected):
    assert chinese_remainder_theorem(numbers, remainders) == expected


##################################################################################
# Part1
##################################################################################


class BusArrival:
    def __init__(self, arrival, bus, idx=None):
        self.bus = bus
        self.wait_time = BusArrival.calc_wait_time(arrival, bus)
        self.idx = idx

    @staticmethod
    def calc_wait_time(arrival, bus):
        rem = arrival % bus
        return bus - rem

    def __lt__(self, other):
        return self.wait_time < other.wait_time

    def metric(self):
        return self.bus * self.wait_time


def calculate_deparature_time_part1(lines):
    iterator = iter(lines)
    arrival = int(next(iterator))

    buses = next(iterator).split(",")
    buses = [int(x) for x in buses if x != "x"]

    bus_arrival = BusArrival(arrival, buses[0])

    for bus in buses[1:]:
        bus_arrival = min(bus_arrival, BusArrival(arrival, bus))

    return bus_arrival.metric()


BASE_TEST = [
    "939",
    "7,13,x,x,59,x,31,19",
]


@pytest.mark.parametrize(
    'lines,expected',
    [
        (BASE_TEST, 295),
    ],
)
def test_calculate_deparature_time_part1(lines, expected):
    assert calculate_deparature_time_part1(lines) == expected


##################################################################################
# Part2
##################################################################################
def shuttle_company_contest_naive(lines):
    iterator = iter(lines)

    # important to skip 1st line
    _ = next(iterator)

    buses = next(iterator).split(",")
    buses = {int(x): i for i, x in enumerate(buses) if x != "x"}

    max_bus = max(buses.keys())
    max_bus_idx = buses[max_bus]
    min_bus = min(buses.keys())

    del buses[max_bus]

    current_timestamp = max_bus

    while True:
        # print("current_timestamp = {}".format(current_timestamp))

        buses_are_good = True

        for bus, idx in buses.items():
            # print("{} {}".format(bus, idx))
            if (current_timestamp - max_bus_idx + idx) % bus != 0:
                buses_are_good = False
                break

        if buses_are_good:
            return current_timestamp - max_bus_idx

        current_timestamp += max_bus

    return current_timestamp


def shuttle_company_contest_part2_fast(lines):
    iterator = iter(lines)

    # important to skip 1st line
    _ = next(iterator)

    buses_str = next(iterator)

    buses = []
    buses_idxs = []

    for i, bus in enumerate(buses_str.split(",")):
        if bus == "x":
            continue

        # second bus 1 minute later -> remainder of minutes is -1
        buses_idxs.append(-i)
        buses.append(int(bus))

    return chinese_remainder_theorem(buses, buses_idxs)


BASE_TEST_PART2 = [
    (
        [
            "939",
            "7,13",
        ],
        77,  # 77 78
    ),
    (
        [
            "939",
            "7,x,13",
        ],
        63,  # 63 65
    ),
    (BASE_TEST, 1068781),
]


@pytest.mark.parametrize('lines,expected', BASE_TEST_PART2)
def test_shuttle_company_contest_naive(lines, expected):
    assert shuttle_company_contest_naive(lines) == expected


@pytest.mark.parametrize('lines,expected', BASE_TEST_PART2)
def test_shuttle_company_contest_part2_fast(lines, expected):
    assert shuttle_company_contest_part2_fast(lines) == expected


if __name__ == "__main__":
    # num = calculate_deparature_time_part1(sys.stdin)
    num = shuttle_company_contest_part2_fast(sys.stdin)
    print("{0}".format(num))
