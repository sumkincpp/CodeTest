#!/usr/bin/env python

import sys
import pytest

from collections import namedtuple


def is_pass_valid(line):
    start, word = line.strip().split(": ")

    rules = {}

    Rule = namedtuple('Rule', ['min', 'max'])

    for rule in start.split(","):
        rule = rule.strip()
        letter = rule[-1]
        min_c, max_c = map(int, rule[:-1].strip().split("-"))

        rules[letter] = Rule(min_c, max_c)

    lookup = {}

    for letter in word:
        lookup.setdefault(letter, 0)
        lookup[letter] += 1

    # print(lookup)

    for letter, rule in rules.items():

        if letter not in lookup:
            return False

        if lookup[letter] > rule.max:
            return False

        if lookup[letter] < rule.min:
            return False

    return True


def is_pass_valid_2(line):
    start, word = line.strip().split(": ")

    rules = {}

    Rule = namedtuple('Rule', ['min', 'max'])

    for rule in start.split(","):
        rule = rule.strip()
        letter = rule[-1]
        min_c, max_c = map(int, rule[:-1].strip().split("-"))

        rules[letter] = Rule(min_c, max_c)

    for rule_letter, rule in rules.items():
        lookup = {}

        for idx in (rule.max, rule.min):
            if idx < 1 or idx > len(word):
                raise IndexError(word, idx)

            letter = word[idx - 1]

            lookup.setdefault(letter, 0)
            lookup[letter] += 1

        if len(lookup) != 2:
            return False

        if rule_letter not in lookup:
            return False

    return True


def find_max_invalid_passwords(iterator, validate_password=is_pass_valid):
    valid_passwords = 0

    for line in iterator:
        if validate_password(line):
            valid_passwords += 1

    return valid_passwords


@pytest.mark.parametrize('lines,expected', [
    (
        [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc"
        ],
        2
    ),
    (
        [
            "4-10 m: mmmjmmmmmmmm",
            "15-17 s: sssssssssssssshsmss",
            "8-10 q: qqwwktqtqsqtb",
            "3-4 n: nbxnn"
        ],
        2
    )
])
def test_find_max_invalid_passwords(lines, expected):
    assert find_max_invalid_passwords(lines) == expected


@pytest.mark.parametrize('lines,expected', [
    (
        [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc"
        ],
        1
    ),
    (
        [
            "2-3 p: pppppp",
            "4-9 g: gmfgxgsgg",
            "3-5 n: fnnhnn",
            "6-7 j: gbdjhrjh",
        ],
        1
    ),
    (
        [
            "1-3 d: dddd",
            "3-5 j: jjjkj"
        ],
        0
    )
])
def test_find_max_is_pass_valid_2(lines, expected):
    assert find_max_invalid_passwords(lines, is_pass_valid_2) == expected


if __name__ == "__main__":
    num = find_max_invalid_passwords(sys.stdin, is_pass_valid_2)
    print("{0}".format(num))
