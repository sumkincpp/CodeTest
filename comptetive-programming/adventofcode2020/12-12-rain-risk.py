#!/usr/bin/env python
#
# Q:      How many WASPs does it take to change a light bulb?
# A:      One.
#

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


DIRECTIONS = [
    MoveDirection.NORTH,
    MoveDirection.WEST,
    MoveDirection.SOUTH,
    MoveDirection.EAST,
]
NUM_DIRECTIONS = len(DIRECTIONS)

# 0 -> no rotate
# 1 -> right
# -1 -> left
ROTATION = [
    [(1, 0), (0, 1)],
    [(0, -1), (1, 0)],  # 90
    [(-1, 0), (0, -1)],
    [(0, 1), (-1, 0)],  # 270
]


def ship_moves_manhattan_distance(moves):
    x = 0
    y = 0

    curr_dir = MoveDirection.EAST

    for line in moves:
        matches = re.match(r"^([A-Z]+)([0-9]+)$", line)

        new_dir = matches.group(1)
        step = int(matches.group(2))

        if new_dir == MoveDirection.LEFT:
            curr_idx = DIRECTIONS.index(curr_dir)
            curr_dir = DIRECTIONS[(curr_idx + step // 90) % NUM_DIRECTIONS]
        elif new_dir == MoveDirection.RIGHT:
            curr_idx = DIRECTIONS.index(curr_dir)
            curr_dir = DIRECTIONS[(curr_idx - step // 90) % NUM_DIRECTIONS]
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


def waypoint_moves_manhattan_distance(moves):
    """
    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.
    """

    # waypoint
    wx = 10
    wy = 1

    # our ship
    x = 0
    y = 0

    for line in moves:
        print(line)
        matches = re.match(r"^([A-Z]+)([0-9]+)$", line)

        new_dir = matches.group(1)
        step = int(matches.group(2))

        if new_dir == MoveDirection.LEFT:
            matrix = ROTATION[(+step // 90) % NUM_DIRECTIONS]

            wx2 = wx * matrix[0][0] + wy * matrix[0][1]
            wy2 = wx * matrix[1][0] + wy * matrix[1][1]

            wx, wy = wx2, wy2
        elif new_dir == MoveDirection.RIGHT:
            matrix = ROTATION[(-step // 90) % NUM_DIRECTIONS]

            wx2 = wx * matrix[0][0] + wy * matrix[0][1]
            wy2 = wx * matrix[1][0] + wy * matrix[1][1]

            wx, wy = wx2, wy2
        else:
            # moving forward
            if new_dir == MoveDirection.FORWARD:
                x += wx * step
                y += wy * step
            elif new_dir == MoveDirection.NORTH:
                wy += step
            elif new_dir == MoveDirection.SOUTH:
                wy -= step
            elif new_dir == MoveDirection.WEST:
                wx -= step
            elif new_dir == MoveDirection.EAST:
                wx += step
            else:
                raise ValueError("What' up?")

        print("x={} y={} wx={} wy={}".format(x, y, wx, wy))

    print("x={} y={}".format(x, y))

    return abs(x) + abs(y)


@pytest.mark.parametrize(
    'lines,expected',
    [
        (BASE_TEST, 25),
    ],
)
def test_ship_moves_manhattan_distance(lines, expected):
    assert ship_moves_manhattan_distance(lines) == expected


@pytest.mark.parametrize(
    'lines,expected',
    [
        (BASE_TEST, 286),
    ],
)
def test_waypoint_moves_manhattan_distance(lines, expected):
    assert waypoint_moves_manhattan_distance(lines) == expected


if __name__ == "__main__":
    num = waypoint_moves_manhattan_distance(sys.stdin)
    print("{0}".format(num))
