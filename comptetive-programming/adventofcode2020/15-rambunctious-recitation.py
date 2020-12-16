#!/usr/bin/env python
#
#
import re
import sys
import math

from functools import reduce
import operator
from typing import Dict

from collections import defaultdict
import pytest


class SeenNumber:
    def is_once(self):
        raise NotImplementedError()

    def next_number(self):
        raise NotImplementedError()


class SeenManyNumber(SeenNumber):
    def __init__(self, a, b):
        # But actually no need in condition
        if a > b:
            self.a, self.b = b, a
        else:
            self.a, self.b = a, b

    def is_once(self):
        return False

    def promote(self, b):
        return SeenManyNumber(self.b, b)

    def next_number(self):
        return self.b - self.a

    def __repr__(self):
        return f"SeenManyNumber({self.a}, {self.b})"


class SeenOnceNumber(SeenNumber):
    def __init__(self, a):
        self.a = a

    def promote(self, b):
        return SeenManyNumber(self.a, b)

    def is_once(self):
        return True

    def next_number(self):
        return 0

    def __repr__(self):
        return f"SeenOnceNumber({self.a})"


def rambunctious_recitation(lines, num):
    numbers = [int(x) for x in next(iter(lines)).split(",")]

    seen_numbers = {}

    i = 0
    for n in numbers:
        seen_numbers[n] = SeenOnceNumber(i)
        i += 1

    last_number = numbers[-1]

    for j in range(i, num):
        if j % 1000000 == 0:
            print(j)

        next_number = seen_numbers[last_number].next_number()

        # print(f"Last number is {last_number}")
        # print(f"New number is {next_number}")

        if next_number not in seen_numbers:
            seen_numbers[next_number] = SeenOnceNumber(j)
        else:
            seen_numbers[next_number] = seen_numbers[next_number].promote(j)

        # print(seen_numbers)

        last_number = next_number

    # print(numbers)

    return last_number


@pytest.mark.parametrize(
    "start,num,expected",
    [
        (["0,3,6"], 10, 0),
        (["1,3,2"], 2020, 1),
        (["2,1,3"], 2020, 10),
        (["1,2,3"], 2020, 27),
        (["2,3,1"], 2020, 78),
    ],
)
def test_rambunctious_recitation(start, num, expected):
    assert rambunctious_recitation(start, num) == expected


if __name__ == "__main__":
    # 758
    # That's the right answer! You are one gold star closer to saving your vacation. [Continue to Part Two]
    # num = rambunctious_recitation(sys.stdin, 2020)

    # 814
    # That's the right answer! You are one gold star closer to saving your vacation.
    # You have completed Day 15! You can [Share] this victory or [Return to Your Advent Calendar].

    # real    1m22.240s
    # user    1m19.641s
    # sys     0m2.531s

    num = rambunctious_recitation(sys.stdin, 30000000)
    print("{0}".format(num))
