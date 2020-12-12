#!/usr/bin/env python
# You are the only person to ever get this message.

import re
import sys
import pytest
import operator

from enum import Enum
from functools import reduce

from typing import List

from collections import namedtuple, OrderedDict, defaultdict


BASE_TEST = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


class MoveDirection(str, Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    FORWARD = "F"
    RIGHT = "R"
    LEFT = "L"


def ship_moves_manhattan_distance(moves):
    dirs = [
        MoveDirection.NORTH,
        MoveDirection.WEST,
        MoveDirection.SOUTH,
        MoveDirection.EAST,
    ]
    num_dir = len(dirs)
    # left_dirs = {d: dirs[(i + 1) % len(dirs)] for i, d in enumerate(dirs)}
    # right_dirs = {d: dirs[i - 1] for i, d in enumerate(dirs)}

    # print(left_dirs)
    # print(right_dirs)

    # sys.exit(0)

    x = 0
    y = 0

    curr_dir = MoveDirection.EAST

    for line in moves:
        matches = re.match(r"^([A-Z]+)([0-9]+)$", line)

        new_dir = matches.group(1)
        step = int(matches.group(2))

        if new_dir == MoveDirection.LEFT:
            curr_idx = dirs.index(curr_dir)
            curr_dir = dirs[(curr_idx + step // 90) % num_dir]
        elif new_dir == MoveDirection.RIGHT:
            curr_idx = dirs.index(curr_dir)
            curr_dir = dirs[(curr_idx - step // 90) % num_dir]
        else:
            # When moving forward,
            # - translate new_dir to use curr_dir
            if new_dir == MoveDirection.FORWARD:
                new_dir = curr_dir

            if new_dir == MoveDirection.NORTH:
                y += step
            elif new_dir == MoveDirection.SOUTH:
                y -= step
            elif new_dir == MoveDirection.WEST:
                x -= step
            elif new_dir == MoveDirection.EAST:
                x += step
            else:
                raise ValueError("What' up?")

        print("x={} y={} dir={}".format(x, y, curr_dir))

    print("x={} y={} dir={}".format(x, y, curr_dir))

    return abs(x) + abs(y)


@pytest.mark.parametrize(
    'lines,expected',
    [
        (BASE_TEST, 25),
    ],
)
def test_ship_moves_manhattan_distance(lines, expected):
    assert ship_moves_manhattan_distance(lines) == expected


if __name__ == "__main__":
    num = ship_moves_manhattan_distance(sys.stdin)
    print("{0}".format(num))
