#!/usr/bin/env python

import sys
import pytest

ADVENT_2020 = 2020


def find_max_product_simple(iterator, numbers_count=2, desired_num=ADVENT_2020):
    """
    Finds max product of TWO nums that are also in sum= :desired_num
    """
    lookup = {}
    max_so_far = -1

    for line in iterator:
        num1 = int(line)
        num2 = desired_num - num1

        if num1 in lookup:
            new_product = num1 * num2

            if max_so_far < new_product:
                max_so_far = new_product

        lookup.setdefault(num2, 1)

    return max_so_far


def find_max_product(iterator, numbers_count=2, desired_num=ADVENT_2020):
    # generation(0 to numbers_count - 2)
    lookup = {i: dict() for i in range(numbers_count - 1)}
    max_so_far = -1

    for line in iterator:
        num1 = int(line)
        num2 = (desired_num - num1)

        if num2 in lookup[numbers_count - 2]:
            new_product = lookup[numbers_count - 2][num2] * num1

            if max_so_far < new_product:
                max_so_far = new_product

        # promoting generations
        for i in range(1, numbers_count - 1):
            for val, product in lookup[i - 1].items():
                lookup[i].setdefault(val + num1, num1 * product)

        lookup[0].setdefault(num1, num1)

    print(lookup)

    return max_so_far


@pytest.mark.parametrize('numbers,expected', [
    ([1], -1),
    ([2019, 1], 2019),
    ([2019, 1, 2018, 2], 4036),
    ([1721,
      979,
      366,
      299,
      675,
      1456], 514579),
])
def test_find_max_product(numbers, expected):
    assert find_max_product(numbers) == expected


@pytest.mark.parametrize('numbers,expected', [
    ([1, 2, 3], -1),
    ([1, 2, 2017], 4034),
    ([1721,
      979,
      366,
      299,
      675,
      1456], 241861950),
])
def test_find_max_product_3(numbers, expected):
    assert find_max_product(numbers, 3) == expected


if __name__ == "__main__":
    num = find_max_product(sys.stdin, 3)
    print("{0}".format(num))
