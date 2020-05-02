import fileinput

import re
import math


NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3


def can_reach_pp(X, Y, pp_steps):
    x, y = X, Y
    min_x = None

    coords = []

    for i, step in enumerate(pp_steps):
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        elif step == 'W':
            x -= 1

        steps_needed = abs(x) + abs(y)

        #print("{} {} i={} sum={}".format(x, y, i, abs(x) + abs(y)))

        if steps_needed == i + 1 or steps_needed == i:
            return i + 1

    return "IMPOSSIBLE"


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        X, Y, pp_steps = map(str, next(finput).strip().split())
        X = int(X)
        Y = int(Y)

        res = can_reach_pp(X, Y, pp_steps)

        print('Case #{}: {}'.format(case_no, res))


if __name__ == '__main__':
    main()
