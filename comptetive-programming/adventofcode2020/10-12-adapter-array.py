#!/usr/bin/env python
# When in doubt, tell the truth.
#                 -- Mark Twain

import sys
import pytest
import operator

from functools import reduce

from typing import List

from collections import namedtuple, OrderedDict


def read_int_list(lines):
    iterator = iter(lines)

    data = []

    for line in iterator:
        num = int(line)

        data.append(num)

    return data


def find_jolts(lines):
    adapters = read_int_list(lines)
    adapters = sorted(adapters)

    jolts = {1: 1, 3: 1}

    # for inc in jolts.keys():
    #     for a in adapters:
    #         rem = a % inc
    #         print("{} {} {:3d} and {:3d}".format(inc, rem, a, a + inc))

    for i in range(0, len(adapters) - 1):
        diff = abs(adapters[i] - adapters[i + 1])

        jolts.setdefault(diff, 0)
        jolts[diff] += 1

    print(jolts)

    return jolts[1] * jolts[3]


def find_jolts_variants(lines):
    adapters = read_int_list(lines)
    adapters = sorted(adapters)

    print(adapters)

    return calculate_continuos(adapters)


BASE_TEST = [
    "16",
    "10",
    "15",
    "5",
    "1",
    "11",
    "7",
    "19",
    "6",
    "12",
    "4",
]

BASE_TEST2 = [
    "28",
    "33",
    "18",
    "42",
    "31",
    "14",
    "46",
    "20",
    "48",
    "47",
    "24",
    "23",
    "49",
    "45",
    "19",
    "38",
    "39",
    "11",
    "1",
    "32",
    "25",
    "35",
    "8",
    "17",
    "7",
    "9",
    "4",
    "2",
    "34",
    "10",
    "3",
]


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            35,
        ),
        (
            BASE_TEST2,
            220,
        ),
    ],
)
def test_find_jolts(lines, expected):
    assert find_jolts(lines) == expected


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            8,
        ),
        (
            BASE_TEST2,
            19208,
        ),
    ],
)
def test_find_jolts_variants(lines, expected):
    assert find_jolts_variants(lines) == expected


def calculate_continuos(
    adapters: List[int],
    prev_num=0,
    max_len: int = 3,
    idx: int = 0,
    quick_cache=None,
) -> int:
    """
    Calculate adapters count
    """
    # print("calculate_continuos: {} + {} / {} ".format(adapters[idx:], prev_num))

    total_adapters = len(adapters)

    if total_adapters - idx == 1:
        # first too big jump case -> count =0
        return int(prev_num + max_len >= adapters[idx])
    elif total_adapters - idx < 1:
        return 1

    if quick_cache is None:
        quick_cache = {}
    elif idx in quick_cache:
        return quick_cache[idx]

    total_count = 0

    j = idx
    while j < len(adapters):
        current = adapters[j]

        # Ooops, too big jump
        if current > prev_num + max_len:
            break

        count = calculate_continuos(adapters, current, max_len, j + 1, quick_cache)

        total_count += count
        j += 1

    quick_cache.setdefault(idx, total_count)

    return total_count


@pytest.mark.parametrize(
    'numbers,expected',
    [
        # too big first jumps
        ([6], 0),
        ([5, 10], 0),
        # thats simple cases
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 4),
        ([1, 2, 3, 4], 7),
        ([1, 2, 3, 4, 5], 13),
        ([1, 2, 3, 4, 5, 6], 24),
        # that mixed jump case
        ([1, 4, 5, 6, 7], 4),
        # 1, 4, 7, 10, 11
        # 1, 4, 5, 6, 7, 10, 11
        # 1, 4, 5, 7, 10, 11
        # 1, 4, 6, 7, 10, 11
        ([1, 4, 5, 6, 7, 10, 11], 4),
        ([1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19], 8),
    ],
)
def test_calculate_continuos(numbers, expected):
    assert calculate_continuos(numbers) == expected


if __name__ == "__main__":
    num = find_jolts_variants(sys.stdin)
    print("{0}".format(num))
