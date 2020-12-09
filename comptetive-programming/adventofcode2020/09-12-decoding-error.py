#!/usr/bin/env python
# Bridge ahead.  Pay troll.
import sys
import copy
import pytest

from collections import namedtuple


def find_decoding_error(iterator, preamble_length=26):
    iterator = iter(iterator)

    last_numbers = [int(next(iterator)) for i in range(0, preamble_length)]

    lookup = {}

    for i in range(0, len(last_numbers)):
        n1 = last_numbers[i]

        for j in range(i + 1, len(last_numbers)):
            n2 = last_numbers[j]
            sum_ = n1 + n2

            lookup.setdefault(sum_, 0)
            lookup[sum_] += 1

    for line in iterator:
        new_num = int(line)

        if new_num not in lookup:
            return new_num

        prev_num = last_numbers[0]

        for i in range(1, len(last_numbers)):
            sum_ = prev_num + last_numbers[i]
            lookup[sum_] -= 1

            if lookup[sum_] == 0:
                del lookup[sum_]

        for j in range(1, len(last_numbers)):
            n2 = last_numbers[j]
            sum_ = n2 + new_num

            lookup.setdefault(sum_, 0)
            lookup[sum_] += 1

        last_numbers.pop(0)
        last_numbers.append(new_num)

    return -1


DistanceSum = namedtuple("DistanceSum", "min,max,i,j")


def find_decoding_error_ex(iterator, preamble_length=26):
    iterator = iter(iterator)

    last_numbers = [int(next(iterator)) for i in range(0, preamble_length)]

    contiguous_sum = {}

    # a map of right borders/grenzen to sums in list -> can remove if no match
    partial_sum = {}

    numbers = copy.copy(last_numbers)

    # Calculating (i,j) sums, also partial tracking separately
    for i in range(0, len(last_numbers)):
        for j in range(i + 1, len(last_numbers)):
            sum_ = sum(last_numbers[i : j + 1])
            min_ = min(last_numbers[i : j + 1])
            max_ = max(last_numbers[i : j + 1])

            item = DistanceSum(min_, max_, i, j)

            if j == len(last_numbers) - 1:
                partial_sum.setdefault(sum_, item)

                # Property of growth, Ja?
                assert partial_sum[sum_] == item, "That' strange! Is it /0/?"
            else:
                contiguous_sum.setdefault(sum_, set())
                contiguous_sum[sum_].add(item)

    lookup = {}

    for i in range(0, len(last_numbers)):
        n1 = last_numbers[i]

        for j in range(i + 1, len(last_numbers)):
            n2 = last_numbers[j]
            sum_ = n1 + n2

            lookup.setdefault(sum_, 0)
            lookup[sum_] += 1

    idx = len(last_numbers)

    for line in iterator:
        new_num = int(line)

        numbers.append(new_num)

        if new_num not in lookup:
            print(f"No value for {new_num} in lookup")

            # This is simple, but not so fast!
            # for i in range(0, len(numbers)):
            #     for j in range(i + 1, len(numbers)):
            #         rng = numbers[i : j + 1]

            #         min_, max_ = min(rng), max(rng)

            #         if sum(rng) == new_num:
            #             print("{} {} {} {}".format(i, j, min_, max_))
            #             return min_ + max_

            if new_num in partial_sum:
                item = partial_sum[new_num]
            else:
                item = contiguous_sum[new_num]
                item = next(iter(item))

            return item.min + item.max

        # print(partial_sum)

        # Reintegrating partial sums as complete contiguous range sums
        for sum_ in partial_sum:
            contiguous_sum.setdefault(sum_, set()).add(partial_sum[sum_])

        # in last partial sums last element was not participate,
        # we take him as circa new full sum + new elem
        last_number = last_numbers[-1]

        partial_sum[last_number] = DistanceSum(
            last_number,
            last_number,
            idx - 1,
            idx - 1,
        )

        # Calculating new border partial sums
        new_partials = {}

        for sum_ in partial_sum.keys():
            contiguous_sum.setdefault(sum_, set()).add(partial_sum[sum_])

            prev_item = partial_sum[sum_]

            new_sum = sum_ + new_num

            new_item = DistanceSum(
                min(prev_item.min, new_num),
                max(prev_item.max, new_num),
                prev_item.i,
                prev_item.j + 1,
            )

            new_partials.setdefault(new_sum, new_item)

        partial_sum = new_partials

        prev_num = last_numbers[0]
        for i in range(1, len(last_numbers)):
            sum_ = prev_num + last_numbers[i]
            lookup[sum_] -= 1

            if lookup[sum_] == 0:
                del lookup[sum_]

        for j in range(1, len(last_numbers)):
            n2 = last_numbers[j]
            sum_ = n2 + new_num

            lookup.setdefault(sum_, 0)
            lookup[sum_] += 1

        last_numbers.pop(0)
        last_numbers.append(new_num)

        idx += 1

    return -1


BASE_DATA = [
    "35",
    "20",
    "15",
    "25",
    "47",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576",
]


@pytest.mark.parametrize(
    'lines,preamble_length,expected',
    [
        (
            BASE_DATA,
            5,
            127,
        )
    ],
)
def test_find_max_product(lines, preamble_length, expected):
    assert find_decoding_error(lines, preamble_length) == expected


@pytest.mark.parametrize(
    'lines,preamble_length,expected',
    [
        (
            BASE_DATA,
            5,
            62,
        ),
        (
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "15",
            ],
            5,
            6,
        ),
        (
            [
                "1",
                "3",
                "2",
                "14",
                "15",
                "6",
            ],
            5,
            4,
        ),
        (
            [
                "2222",
                "1111",
                "1",
                "2",
                "3",  # -----
                "6",
            ],
            5,
            4,
        ),
        (
            [
                "2222",
                "10",
                "1",
                "2",
                "3333",  # -----
                "13",
            ],
            5,
            11,
        ),
        (
            [
                "10",
                "21",
                "33",
                "100000",
                "7",
                "28",
                "28",
                "64",
            ],
            5,
            43,
        ),
    ],
)
def test_find_max_product_ex(lines, preamble_length, expected):
    assert find_decoding_error_ex(lines, preamble_length) == expected


if __name__ == "__main__":
    num = find_decoding_error_ex(
        sys.stdin, int(sys.argv[1]) if len(sys.argv) > 1 else 26
    )
    print("{0}".format(num))
