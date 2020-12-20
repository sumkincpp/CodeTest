import re
import sys
import copy
import pytest

from collections import namedtuple, defaultdict

Tile = namedtuple("Tile", "num,dirs")


def lst_to_int(lst):
    return int(str("".join(str(int(l == "#")) for l in lst)), 2)


def parse_tile(iter):
    match = re.match(r"Tile ([0-9]+):", next(iter))

    number = int(match.group(1))

    top_line = list(next(iter).strip())
    left_line = [top_line[0]]
    right_line = [top_line[-1]]

    for i in range(0, len(top_line) - 2):
        next_line = next(iter).strip()

        left_line.append(next_line[0])
        left_line.append(next_line[-1])

    bottom_line = list(next(iter).strip())
    left_line.append(bottom_line[0])
    right_line.append(bottom_line[-1])

    dirs = tuple(
        lst_to_int(d)
        for d in (top_line, bottom_line, left_line, right_line)
    )

    return Tile(number, dirs)


def jurrasic_jigsaw(data):
    tiles = defaultdict(set)

    tiles_list = []

    data_iter = iter(data)

    while True:
        tile = parse_tile(data_iter)

        try:
            assert next(data_iter).strip() == ""
        except StopIteration:
            break

        print(tile)

        if not tile:
            break

        tiles_list.append(tile)

        for d in tile.dirs:
            tiles[d].update(tile)

    for i, tls in sorted(tiles.items(), key=lambda x: x[0]):
        print("{}: {}".format(i, tls))

    # print(dict(tiles))

    return 0


if __name__ == "__main__":
    num = jurrasic_jigsaw(sys.stdin)
    print("{0}".format(num))
