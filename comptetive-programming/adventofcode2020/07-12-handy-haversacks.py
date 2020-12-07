#!/usr/bin/env python

import re
import sys
import pytest
import logging
import math

from collections import namedtuple

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
)

logger = logging.getLogger()

Bag = namedtuple("Bag", "count,art")


def match_bag(bag_str):
    if bag_str.startswith("no other bags"):
        return None

    m = re.match(r'^\s*([0-9])+ ([\w ]+) bags?\.?$', bag_str)

    if not m:
        raise ValueError(f"Ooops! Bag matcher not working for '{bag_str}'")

    return Bag(count=int(m.group(1)), art=m.group(2))


def contains_bag_of_art(bags, bag_lookup, art):
    curr_bags = bags

    print(f"bags = {bags}")

    while len(curr_bags) > 0:
        if art in curr_bags:
            print("Found {} in curr_bags".format(art))
            return 1

        new_bags = {}

        for b in curr_bags:
            new_bags.update(bag_lookup[b])

        curr_bags = new_bags

    return 0


def calculate_bags(iterator, art="shiny gold"):
    bags = {}

    for line in iterator:
        line = line.strip()

        bag_str, containment = line.split(" contain ")

        bag_art = bag_str.replace(" bags", "")

        cbags = [match_bag(b) for b in containment.split(",")]
        cbags = {c.art: c for c in cbags if c}

        bags[bag_art] = cbags

    total_bags = sum(contains_bag_of_art(b, bags, art) for b in bags.values())

    return total_bags


def total_bags(iterator, art="shiny gold"):
    bags_lookup = {}

    for line in iterator:
        line = line.strip()

        bag_str, containment = line.split(" contain ")

        bag_art = bag_str.replace(" bags", "")

        cbags = [match_bag(b) for b in containment.split(",")]
        cbags = {c.art: c for c in cbags if c}

        bags_lookup[bag_art] = cbags

    curr_bags = [[1, art]]

    total_bags = 0

    while len(curr_bags) > 0:
        new_bags = []

        for count, art in curr_bags:
            total_bags += count

            if not bags_lookup[art]:
                continue

            for bag in bags_lookup[art].values():
                new_bags.append([count * bag.count, bag.art])

        curr_bags = new_bags

    return total_bags - 1


BASE_TEST = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            4,
        ),
    ],
)
def test_calculate_bags(lines, expected):
    assert calculate_bags(lines) == expected


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            32,
        ),
        (
            [
                "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                "dark olive bags contain no other bags.",
                "vibrant plum bags contain no other bags.",
            ],
            3,
        ),
        (
            [
                "shiny gold bags contain 1 dark olive bag.",
                "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                "faded blue bags contain no other bags.",
                "dotted black bags contain no other bags.",
            ],
            8,
        ),
        (
            [
                "shiny gold bags contain 2 dark red bags.",
                "dark red bags contain 2 dark orange bags.",
                "dark orange bags contain 2 dark yellow bags.",
                "dark yellow bags contain 2 dark green bags.",
                "dark green bags contain 2 dark blue bags.",
                "dark blue bags contain 2 dark violet bags.",
                "dark violet bags contain no other bags.",
            ],
            126,
        ),
    ],
)
def test_total_bags(lines, expected):
    assert total_bags(lines) == expected


if __name__ == "__main__":
    # num = calculate_bags(sys.stdin)
    num = total_bags(sys.stdin)
    print("{0}".format(num))
