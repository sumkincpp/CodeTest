#!/usr/bin/env python
#
#
import re
import sys
import math
import queue

from functools import reduce
import operator
from typing import Dict

from collections import defaultdict, namedtuple
import pytest


NumberVariant = namedtuple("NumberVariant", "name,ranges")


class Node:
    def __init__(self, interval, meta, max_=None, left=None, right=None):
        self.interval = interval
        self.meta = meta
        self.max = max_
        self.right = right
        self.left = left

    def l(self):
        return self.interval[0]

    def r(self):
        return self.interval[1]

    def print(self, type_="H", indent=0):
        print("{} {} - {} - {}".format(" " * indent, type_, self.interval, self.meta))

        if self.left:
            self.left.print("L", indent + 2)

        if self.right:
            self.right.print("R", indent + 2)


class IntervalTree(object):
    def __init__(self, root):
        self.root = root

    def add_node(self, new_node):
        if self.root == None:
            self.root = new_node
            return

        node = self.root

        while node != None:
            if new_node.l() < node.l():
                if node.left is None:
                    node.left = new_node
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = new_node
                    return
                node = node.right

    def search(self, number):
        nodes = queue.Queue()
        nodes.put(self.root)

        variants = []

        while not nodes.empty():
            node = nodes.get()

            if node is None:
                continue

            if number < node.l():
                nodes.put(node.left)
            else:
                if number <= node.r():
                    variants.append(node.meta)

                nodes.put(node.left)
                nodes.put(node.right)

        return variants

    def is_overlapping(self, interval_left, interval_right):
        return interval_left[0] <= interval_right[1] and \
            interval_right[0] <= interval_left[1]

    def print(self):
        self.root.print()


def ticket_translation(lines):

    lines_iter = iter(lines)

    inv_tree = IntervalTree(None)

    while True:
        line = next(lines_iter).strip()

        if line == "":
            break

        match = re.match(r"([^:]+): (.+)", line)

        if not match:
            raise ValueError("unexpected line {}".format(line))

        name, rhs = match.groups()

        ranges = []

        for part in rhs.split(" or "):
            rng = list(map(int, part.split("-", 1)))

            ranges.append(rng)

        variant = NumberVariant(name, ranges)

        for rng in ranges:
            inv_tree.add_node(Node(rng, variant))

    inv_tree.print()

    assert next(lines_iter).strip() == "your ticket:"

    my_ticket = list(map(int, next(lines_iter).split(",")))

    assert next(lines_iter).strip() == ""
    assert next(lines_iter).strip() == "nearby tickets:"

    invalid_numbers = 0

    for line in lines_iter:
        maybe_a_ticket = list(map(int, line.split(",")))

        # print("Maybe a ticket {}".format(maybe_a_ticket))

        for n in maybe_a_ticket:
            variants = [v.name for v in inv_tree.search(n)]
            if not variants:
                print("s {}".format(n))
                invalid_numbers += n

    return invalid_numbers


def ticket_translation_part2(lines):

    lines_iter = iter(lines)

    inv_tree = IntervalTree(None)

    while True:
        line = next(lines_iter).strip()

        if line == "":
            break

        match = re.match(r"([^:]+): (.+)", line)

        if not match:
            raise ValueError("unexpected line {}".format(line))

        name, rhs = match.groups()

        ranges = []

        for part in rhs.split(" or "):
            rng = list(map(int, part.split("-", 1)))

            ranges.append(rng)

        variant = NumberVariant(name, ranges)
        for rng in ranges:
            inv_tree.add_node(Node(rng, variant))

        print(variant)

    inv_tree.print()

    print("------")
    print(inv_tree.search(870))

    assert next(lines_iter).strip() == "your ticket:"

    my_ticket = list(map(int, next(lines_iter).split(",")))

    assert next(lines_iter).strip() == ""
    assert next(lines_iter).strip() == "nearby tickets:"

    invalid_numbers = 0

    ticket_fields = defaultdict(set)

    maybe_a_tickets = [list(map(int, line.split(","))) for line in lines_iter]

    # maybe_a_tickets.append(my_ticket)

    for maybe_a_ticket in maybe_a_tickets:
        print("Maybe a ticket {}".format(maybe_a_ticket))

        ticket = []

        is_valid = True

        for n in maybe_a_ticket:
            variants = [v.name for v in inv_tree.search(n)]
            if not variants:
                is_valid = False
                # print("s {}".format(n))
                invalid_numbers += n
                break

            # print(" {} {}".format(n, variants))

            ticket.append(variants)

        if is_valid:
            for i, fields in enumerate(ticket):
                # ticket_fields[i].update(set(fields))
                if ticket_fields[i]:
                    ticket_fields[i] &= set(fields)
                else:
                    ticket_fields[i] = set(fields)

    derived_fields = {}

    for key in sorted(ticket_fields.keys(), key=lambda x: len(ticket_fields[x])):

        fields = ticket_fields[key] - set(derived_fields.keys())

        assert len(fields) == 1

        field = next(iter(fields))

        derived_fields[field] = key

        print("{} {}".format(key, ticket_fields[key]))

    print(derived_fields)

    total = 1

    for field, idx in derived_fields.items():
        if field.startswith("departure"):
            total *= my_ticket[idx]

    return total


BASE_TEST = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


@ pytest.mark.parametrize(
    "start,expected",
    [
        (BASE_TEST.splitlines(), 71)
    ],
)
def test_ticket_translation(start, expected):
    assert ticket_translation(start) == expected


if __name__ == "__main__":
    num = ticket_translation_part2(sys.stdin)
    print("{0}".format(num))
