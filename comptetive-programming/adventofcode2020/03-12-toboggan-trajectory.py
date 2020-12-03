#!/usr/bin/env python

import sys
import pytest
import math

from collections import namedtuple


def find_trees_tobogan_trajectory(iterator):
    """
    Finds max product of TWO nums that are also in sum= :desired_num
    """
    x, y = 0, 0
    trees_count = 0

    matrix = [list(line.strip()) for line in iterator]

    print(matrix)

    line_size = len(matrix[0])

    while y < len(matrix):
        trees_count += matrix[y][x % line_size] == "#"

        y += 1
        x += 3

    return trees_count


Trajectory = namedtuple('Trajectory', ['step_x', 'step_y'])


def find_trees_tobogan_trajectory_multiple(iterator, trajectories=None):
    """
    Finds max product of TWO nums that are also in sum= :desired_num
    """
    if not trajectories:
        return 0

    t_count = len(trajectories)

    x, y = [0] * t_count, [0] * t_count

    # trees_count_for_trajectory (traj index -> count)
    trees_count = [0] * t_count

    matrix = [list(line.strip()) for line in iterator]

    line_size = len(matrix[0])

    done_trajectories = set()

    while len(done_trajectories) != len(trajectories):
        for t in range(0, len(trajectories)):
            if t in done_trajectories:
                continue

            if y[t] >= len(matrix):
                done_trajectories.add(t)
                continue

            trees_count[t] += matrix[y[t]][x[t] % line_size] == "#"

            y[t] += trajectories[t].step_y
            x[t] += trajectories[t].step_x

    return math.prod(trees_count)


@pytest.mark.parametrize('lines,expected', [
    ([
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ], 7),
])
def test_find_trees_tobogan_trajectory(lines, expected):
    assert find_trees_tobogan_trajectory(lines) == expected


@pytest.mark.parametrize('lines', [
    (
        [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#",
        ]
    )
])
@pytest.mark.parametrize('trajectories,expected', [
    ([Trajectory(3, 1)], 7),
    ([Trajectory(1, 1)], 2),
    ([Trajectory(7, 1)], 4),
    (
        [
            Trajectory(1, 1),
            Trajectory(3, 1),
            Trajectory(5, 1),
            Trajectory(7, 1),
            Trajectory(1, 2),
        ],
        336
    ),
])
def test_find_trees_tobogan_trajectory_multiple(lines, trajectories, expected):
    assert find_trees_tobogan_trajectory_multiple(lines, trajectories) == expected


if __name__ == "__main__":
    trajectories = [
        Trajectory(1, 1),
        Trajectory(3, 1),
        Trajectory(5, 1),
        Trajectory(7, 1),
        Trajectory(1, 2),
    ]
    num = find_trees_tobogan_trajectory_multiple(sys.stdin, trajectories)

    print("{0}".format(num))
