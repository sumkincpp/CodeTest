#!/usr/bin/env python
# You are the only person to ever get this message.


import sys
import pytest
import operator

from enum import Enum
from functools import reduce

from typing import List

from collections import namedtuple, OrderedDict, defaultdict


class SeatType(str, Enum):
    EMPTY = "L"
    OCCUPIED = "#"
    FLOOR = "."


def get_neihbours(matrix, y, x):
    nbrs = defaultdict(int)

    size_y = len(matrix)
    size_x = len(matrix[0])

    for y_ in range(y - 1, y + 2):
        for x_ in range(x - 1, x + 2):
            if x_ < 0 or x_ >= size_x:
                continue

            if y_ < 0 or y_ >= size_y:
                continue

            if x_ == x and y_ == y:
                # thats seat self
                continue

            seat = matrix[y_][x_]

            nbrs[seat] += 1

    return nbrs


def get_neihbours_first_visible(matrix, y, x):
    nbrs = defaultdict(int)

    size_y = len(matrix)
    size_x = len(matrix[0])

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    directions_count = len(directions)

    occupied_seats = 0
    empty_seats = 0

    i = 1
    while len(directions) > 0:
        new_directions = []

        for direction in directions:
            y_ = y + direction[0] * i
            x_ = x + direction[1] * i

            if x_ < 0 or x_ >= size_x:
                continue

            if y_ < 0 or y_ >= size_y:
                continue

            seat = matrix[y_][x_]

            # print("Checking {} {} {} = {}".format(direction, x_, y_, seat))

            if seat == SeatType.OCCUPIED:
                # print("occupied")
                occupied_seats += 1
            elif seat == SeatType.EMPTY:
                # print("empty")
                empty_seats += 1
            else:
                new_directions.append(direction)

        directions = new_directions
        i += 1

    nbrs[SeatType.OCCUPIED] = occupied_seats

    # not exact right (can be empty or floor)
    nbrs[SeatType.EMPTY] = empty_seats
    nbrs[SeatType.FLOOR] = directions_count - occupied_seats - empty_seats

    return nbrs


def get_new_seat(matrix, y, x):
    """
    Returns new_seat based on 8 neighboring cells
    """
    seat = matrix[y][x]

    new_seat = SeatType(seat)

    if seat == SeatType.EMPTY:
        nbrs = get_neihbours(matrix, y, x)

        if nbrs[SeatType.OCCUPIED] == 0:
            new_seat = SeatType.OCCUPIED
    elif seat == SeatType.OCCUPIED:
        nbrs = get_neihbours(matrix, y, x)

        if nbrs[SeatType.OCCUPIED] >= 4:
            new_seat = SeatType.EMPTY

    return new_seat


def get_new_seat_first_visible(matrix, y, x):
    seat = matrix[y][x]

    new_seat = SeatType(seat)

    if seat == SeatType.EMPTY:
        nbrs = get_neihbours_first_visible(matrix, y, x)

        if nbrs[SeatType.OCCUPIED] == 0:
            new_seat = SeatType.OCCUPIED
    elif seat == SeatType.OCCUPIED:
        nbrs = get_neihbours_first_visible(matrix, y, x)

        if nbrs[SeatType.OCCUPIED] >= 5:
            new_seat = SeatType.EMPTY

    return new_seat


def matrix_evolution_step(matrix, get_new_seat_func=get_new_seat):
    size_y = len(matrix)
    size_x = len(matrix[0])

    state_changed = False

    new_matrix = [[0 for _ in range(0, size_x)] for _ in range(0, size_y)]

    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            seat = matrix[y][x]

            new_seat = get_new_seat_func(matrix, y, x)

            if new_seat.value != seat:
                state_changed = True

            new_matrix[y][x] = new_seat.value

    return new_matrix, state_changed


def seating_system_empty_count(iterator, get_new_seat_func=get_new_seat):

    matrix = []

    for line in iterator:
        matrix.append(list(line.strip()))

    state_changed = True
    i = 0
    while state_changed:
        print(f"Generation {i}")
        for row in matrix:
            print(row)

        matrix, state_changed = matrix_evolution_step(matrix, get_new_seat_func)

        i += 1

    occupied = sum(int(seat == SeatType.OCCUPIED) for row in matrix for seat in row)

    return occupied


BASE_TEST = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]


@pytest.mark.parametrize(
    'lines,expected',
    [
        (BASE_TEST, 37),
    ],
)
def test_seating_system_empty_count(lines, expected):
    assert seating_system_empty_count(lines) == expected


@pytest.mark.parametrize(
    'matrix,y,x,expected',
    [
        pytest.param(
            [
                [".", ".", "."],
                [".", "L", "."],
                [".", ".", "."],
            ],
            1,
            1,
            {"L": 0, "#": 0, ".": 8},
            id="all_empty",
        ),
        pytest.param(
            [
                ["#", "#", "#"],
                ["#", "L", "#"],
                ["#", "#", "#"],
            ],
            1,
            1,
            {"L": 0, "#": 8, ".": 0},
            id="all_occupied",
        ),
        pytest.param(
            [
                ["#", "#", "#", "#"],
                ["#", "L", ".", "#"],
                ["L", ".", ".", "#"],
                ["#", "#", "#", "."],
            ],
            1,
            1,
            {"L": 1, "#": 6, ".": 1},
            id="diagonals_are_complex",
        ),
    ],
)
def test_get_neihbours_first_visible(matrix, y, x, expected):
    res = get_neihbours_first_visible(matrix, y, x)

    print(res)
    assert res == expected


@pytest.mark.parametrize(
    'lines,expected',
    [
        (BASE_TEST, 26),
    ],
)
def test_seating_system_empty_count_first_visible(lines, expected):
    assert seating_system_empty_count(lines, get_new_seat_first_visible) == expected


if __name__ == "__main__":
    num = seating_system_empty_count(sys.stdin, get_new_seat_first_visible)
    print("{0}".format(num))
