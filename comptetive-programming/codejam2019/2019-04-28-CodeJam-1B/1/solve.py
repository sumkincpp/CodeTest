import fileinput

import heapq
import itertools


def move_coord(x, y, dir):

    if dir == 'N':
        return x, y + 1
    if dir == 'S':
        return x, y - 1
    if dir == 'E':
        return x + 1, y
    if dir == 'W':
        return x - 1, y

    raise ValueError(f'[{dir}]')


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        P, Q = map(int, next(finput).strip().split(' '))

        res = 0

        locations = {}

        loc_x = {}
        loc_y = {}

        for move in range(0, P):
            x, y, dir = next(finput).strip().split(' ')
            x, y = int(x), int(y)

            #print('{}', [x, y, dir])
            nx, ny = move_coord(x, y, dir)

            if dir == 'N' or dir == 'S':
                loc_y.setdefault(dir, {}).setdefault(ny, 0)
                loc_y[dir][ny] += 1
            else:
                loc_x.setdefault(dir, {}).setdefault(nx, 0)
                loc_x[dir][nx] += 1

        print(loc_y)
        print(loc_x)
        #
        # possible_x = [item for k, v in loc_x.items() for item in v]
        #
        # min_x = possible_x[0]
        #
        # for x in possible_x:
        #     pass
        #     # for dir, locations in loc_x:
        #     #     for dir, locations in loc_x.items():
        #
        # print(possible_x)

        # pq = []
        # for val in loc_dir:
        #     heapq.heappush(pq, val)
        #
        # # pq2 = []
        # # for val in locations:
        # #     heapq.heappush(pq, val)
        # #
        # # for
        #
        # print("Case #{}: {}".format(case_no, heapq._heappop_max(pq)))


if __name__ == '__main__':
    main()
