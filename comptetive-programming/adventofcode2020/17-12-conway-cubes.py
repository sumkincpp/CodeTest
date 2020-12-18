#!/usr/bin/env python
#
#
import re
import sys
import math
import queue
import itertools

from functools import reduce
from itertools import chain
import operator
from typing import Dict

from collections import defaultdict, namedtuple
import pytest


def level_str_to_matrix_dict(level):
    matrix = {}
    for i, s in enumerate(level):
        row = {i: item
               for i, item in enumerate(s.strip())
               if item == '#'}

        if row:
            matrix[i] = row

    return matrix


def minmax(it):
    min = max = None
    for val in it:
        if min is None or val < min:
            min = val
        if max is None or val > max:
            max = val
    return min, max


def minmax_matrix(data, x):
    if not data:
        return None, None

    return minmax(
        chain.from_iterable([
            data.get(x - 1, {}).keys(),
            data.get(x, {}).keys(),
            data.get(x + 1, {}).keys()
        ]
        )
    )


def get_coord(x_cube, coord):
    curr = x_cube
    for c in coord[:-1]:
        if c not in curr:
            return "."

        curr = curr[c]

    return curr.get(coord[-1], ".")


def set_coord(x_cube, coord, value):
    curr = x_cube
    for c in coord[:-1]:
        curr = curr.setdefault(c, {})

    curr.setdefault(coord[-1], value)


def is_activated(x_cube, coord):
    curr = get_coord(x_cube, coord)

    nbrs = 0

    coords_expanded = [list(range(c - 1, c + 2)) for c in coord]

    for coord in itertools.product(*coords_expanded):
        if get_coord(x_cube, coord) == "#":
            nbrs += 1

    if curr == "#":
        nbrs -= 1

    is_activated = (curr == "#" and nbrs in (2, 3)) \
        or (curr == "." and nbrs == 3)

    return is_activated


def x_cube_level_size(x_cube, dimension):
    it = dimension_values(x_cube, dimension)

    return minmax(it)


def x_cube_level_size_it_conway(x_cube, dimension):
    """
    Special max min version which start from min-1 to max+1,
    that can be used in range
    """
    min_d, max_d = x_cube_level_size(x_cube, dimension)

    return min_d - 1, max_d + 2


def dimension_values(x_cube, level):
    if level < 0:
        raise ValueError("nope")

    if level == 0:
        for v in x_cube.keys():
            yield v
    else:
        for _, sub_cube in x_cube.items():
            for v in dimension_values(sub_cube, level - 1):
                yield v


def flatten(x_cube):
    if isinstance(x_cube, dict):
        for elem in x_cube.values():
            for item in flatten(elem):
                yield item
    else:
        yield x_cube


def coords_iterator(cube, dimensions):
    coords_iterators = []

    for d in range(0, dimensions):
        minmax = x_cube_level_size_it_conway(cube, d)
        coords_iterators.append(range(*minmax))

    return itertools.product(*coords_iterators)

    # total = sum(len(row)
    #             for matrix in cube.values()
    #             for row in matrix.values())


def cube_values(x_cube, dimensions):
    if dimensions < 1:
        raise ValueError("nope")

    if dimensions == 1:
        return len(x_cube)
    else:
        return sum(cube_values(sub_cube, dimensions - 1)
                   for sub_cube in x_cube.values())


def conway_cubes(level0, steps, dimensions=3):
    level = level_str_to_matrix_dict(level0)

    cube = {}

    curr = cube
    for _ in range(0, dimensions - 3):
        curr[0] = {}
        curr = curr[0]

    curr[0] = level

    new_cube = {}

    for i in range(0, steps):
        for coord in coords_iterator(cube, dimensions):
            if is_activated(cube, coord):
                set_coord(new_cube, coord, "#")

        cube = new_cube
        new_cube = {}

    total = cube_values(cube, dimensions)

    return total


@pytest.mark.parametrize("level0,steps,dimension,expected", [
    (""".#.
        ..#
        ###""".splitlines(), 6, 3, 112),
    (""".#.
        ..#
        ###""".splitlines(), 6, 4, 848),
])
def test_conway_cubes(level0, steps, expected, dimension):
    assert conway_cubes(level0, steps, dimension) == expected


if __name__ == "__main__":
    num = conway_cubes(sys.stdin, 6, 4)
    print("{0}".format(num))
