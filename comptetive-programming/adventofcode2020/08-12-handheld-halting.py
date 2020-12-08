#!/usr/bin/env python

import re
import copy
import sys
import pytest
import logging
import math

from enum import Enum

from collections import namedtuple

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
)

logger = logging.getLogger()


class Op(str, Enum):
    nop = "nop"
    acc = "acc"
    jmp = "jmp"


Instruction = namedtuple("Instruction", "op,num")


def parse_inst(line):
    match = re.match(r'^([^ ]+) [+]?(-?[0-9]+)$', line)

    if not match:
        raise ValueError(f"[{line}]")

    return Instruction(match.group(1), int(match.group(2)))


def calcute_accumulate(iterator):
    """

    nop +0  | 0 | 1
    acc +1  | 1 | 2, 8(!)
    jmp +4  | 5 | 3
    acc +3  | 5 | 6
    jmp -3  | 2 | 7
    acc -99 |   |
    acc +1  | 6 | 4
    jmp -4  | 2 | 5 # nop -4
    acc +6  |   |
    """
    iterator = iter(iterator)

    # current instruction line
    instruction_line = 0

    # read instructions so far
    read_instructions = 0

    accumulator = 0

    seen_instructions = {}
    cached_instructions = {}

    while instruction_line not in seen_instructions:
        while read_instructions - 1 < instruction_line:
            try:
                line = next(iterator)
            except StopIteration:
                return accumulator, 0

            line = line.strip()
            cached_instructions[read_instructions] = parse_inst(line)

            read_instructions += 1

        instr = cached_instructions[instruction_line]

        # print(cached_instructions)
        # print(f"instruction = {instr} instruction_line={instruction_line}")

        seen_instructions[instruction_line] = accumulator

        # no need for instruction!
        del cached_instructions[instruction_line]

        if instr.op == Op.jmp:
            instruction_line += instr.num
        elif instr.op == Op.acc:
            instruction_line += 1
            accumulator += instr.num
        elif instr.op == Op.nop:
            instruction_line += 1

    return accumulator, -1


def calcute_accumulate_with_exit(iterator):
    """

    nop +0  | 0 | 1
    acc +1  | 1 | 2, 8(!)
    jmp +4  | 5 | 3
    acc +3  | 5 | 6
    jmp -3  | 2 | 7
    acc -99 |   |
    acc +1  | 6 | 4
    jmp -4  | 2 | 5 # nop -4
    acc +6  |   |
    """
    iterator = iter(iterator)

    # current instruction line
    instruction_line = 0

    # read instructions so far
    read_instructions = 0

    accumulator = 0
    cached_instructions = {}

    for line in iterator:
        cached_instructions[read_instructions] = parse_inst(line)

        read_instructions += 1

    seen_instructions = {}

    while instruction_line not in seen_instructions:
        instr = cached_instructions[instruction_line]

        # print(cached_instructions)
        # print(f"instruction = {instr} instruction_line={instruction_line}")

        seen_instructions[instruction_line] = accumulator

        # no need for instruction!
        del cached_instructions[instruction_line]

        if instr.op == Op.jmp:
            new_acc, exit_code = calculate_to_end(
                instruction_line + 1, seen_instructions, cached_instructions
            )

            if exit_code == 0:
                return new_acc + accumulator

            instruction_line += instr.num
        elif instr.op == Op.acc:
            instruction_line += 1
            accumulator += instr.num
        elif instr.op == Op.nop:
            new_acc, exit_code = calculate_to_end(
                instruction_line + instr.num, seen_instructions, cached_instructions
            )

            if exit_code == 0:
                return new_acc + accumulator

            instruction_line += 1

    return accumulator


def calculate_to_end(instruction_line, seen_instructions, cached_instructions):
    seen_instructions = copy.copy(seen_instructions)
    cached_instructions = copy.copy(cached_instructions)

    accumulator = 0
    while instruction_line not in seen_instructions:
        if instruction_line not in cached_instructions:
            print("Loop break on {}".format(instruction_line))
            return accumulator, 0

        instr = cached_instructions[instruction_line]

        seen_instructions[instruction_line] = accumulator

        # no need for instruction!
        del cached_instructions[instruction_line]

        if instr.op == Op.jmp:
            instruction_line += instr.num
        elif instr.op == Op.acc:
            instruction_line += 1
            accumulator += instr.num
        elif instr.op == Op.nop:
            instruction_line += 1

    return accumulator, -1


BASE_TEST = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",  # nop - 4
    "acc +6",
]


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            5,
        ),
    ],
)
def test_calcute_accumulate(lines, expected):
    assert calcute_accumulate(lines) == (expected, -1)


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            BASE_TEST,
            8,
        ),
    ],
)
def test_calcute_accumulate_with_exit(lines, expected):
    assert calcute_accumulate_with_exit(lines) == expected


if __name__ == "__main__":
    num = calcute_accumulate_with_exit(sys.stdin)
    print("{0}".format(num))
