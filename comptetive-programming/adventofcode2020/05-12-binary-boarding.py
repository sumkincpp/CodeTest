#!/usr/bin/env python

import sys
import pytest
import logging
import math


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
)

logger = logging.getLogger()


def row_id(path):
    return int(
        path.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), 2
    )


def row_ids(iterator):
    curr_max = 0

    for line in iterator:
        line = line.strip()

        curr_max = max(curr_max, row_id(line))

    return curr_max


def missing_seat(iterator):
    seats_found = set()

    for line in iterator:
        line = line.strip()

        seats_found.add(row_id(line))

    for s in seats_found:
        if s + 1 not in seats_found:
            return s + 1

    return -1


@pytest.mark.parametrize(
    'numbers,expected',
    [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_get_row(numbers, expected):
    assert row_id(numbers) == expected


row_id
if __name__ == "__main__":
    num = missing_seat(sys.stdin)
    print("{0}".format(num))
