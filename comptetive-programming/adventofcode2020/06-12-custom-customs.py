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


def calculate_persons(iterator):
    persons_count = 0

    # question answered yes in group
    questions = set()

    for line in iterator:
        line = line.strip()

        if not line:
            # print(questions)

            persons_count += len(questions)

            questions = set()
            continue

        questions.update(line)

    if questions:
        # print(questions)

        persons_count += len(questions)

        questions = set()

    return persons_count


def calculate_persons_everyone_yes(iterator):
    persons_count = 0

    # question answered yes in group
    questions = dict()
    group_size = 0

    for line in iterator:
        line = line.strip()

        if not line:
            persons_count += sum(int(v == group_size) for v in questions.values())

            questions = dict()
            group_size = 0
            continue

        for letter in line:
            questions.setdefault(letter, 0)
            questions[letter] += 1

        group_size += 1

    if questions:
        persons_count += sum(int(v == group_size) for v in questions.values())

    return persons_count


BASE_TEST = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
]


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            11,
        ),
    ],
)
def test_calculate_persons(lines, expected):
    assert calculate_persons(lines) == expected


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            6,
        ),
    ],
)
def test_calculate_persons_everyone_yes(lines, expected):
    assert calculate_persons_everyone_yes(lines) == expected


if __name__ == "__main__":
    num = calculate_persons_everyone_yes(sys.stdin)
    print("{0}".format(num))
