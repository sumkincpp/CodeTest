import fileinput

import re
import math


NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3


def dir_to_r(direction, should_reverse_x, should_reverse_y):

    if direction == NORTH or direction == SOUTH:
        if ((direction == NORTH and should_reverse_y) or
                (direction == SOUTH and not should_reverse_y)):
            return "S"
        else:
            return "N"

    if ((direction == EAST and should_reverse_x) or
            (direction == WEST and not should_reverse_x)):
        return "W"
    else:
        return "E"


def dir_list_to_str(dir_list, should_reverse_x, should_reverse_y):
    return "".join(dir_to_r(c, should_reverse_x, should_reverse_y) for c in dir_list)


def get_jumps(coord_x, coord_y):
    x = list(reversed('{0:b}'.format(coord_x)))
    y = list(reversed('{0:b}'.format(coord_y)))

    jumps = []

    # print("{}; {}".format(coord_x, coord_y))

    # print(x)
    # print(y)
    # print("---------")

    should_reverse_x, should_reverse_y = False, False

    if x and x[-1] == "-":
        should_reverse_x = True
        x.pop()

    if y and y[-1] == "-":
        should_reverse_y = True
        y.pop()

    # print(x)
    # print(y)

    i = 0
    while i < len(x) and i < len(y):
        # print("i = {} x_i={} y_i={}".format(i, x[i], y[i]))
        # print("x = {}".format(x))
        # print("y = {}".format(y))

        if x[i] == "1" and y[i] == "1":
            # print("complex jump")
            # print(x[i-1])
            # print(y[i-1])

            if i > 0 and x[i - 1] == "1":
                jumps.pop()
                jumps.extend([SOUTH, NORTH, WEST])
                y[i] = "0"
                x[i] = "0"
                if y[i - 1] == "1":
                    return "IMPOSSIBLE"

                i += 1
            elif i > 0 and y[i - 1] == "1":
                jumps.pop()
                jumps.extend([SOUTH, EAST, NORTH])
                y[i] = "0"
                x[i] = "0"

                if x[i - 1] == "1":
                    return "IMPOSSIBLE"

                i += 1
            else:
                return "IMPOSSIBLE"

        elif y[i] == "1":
            jumps.append(NORTH)
        elif x[i] == "1":
            jumps.append(EAST)
        else:
            return "IMPOSSIBLE"

        i += 1

    j = i
    while j < len(x):
        if x[j] == "1":
            jumps.append(EAST)
        else:
            return "IMPOSSIBLE"

        j += 1

    j = i
    while j < len(y):
        if y[j] == "1":
            jumps.append(NORTH)
        else:
            return "IMPOSSIBLE"

        j += 1

    # print("jumps -- " + str(jumps))

    return dir_list_to_str(jumps, should_reverse_x, should_reverse_y)

    return "IMPOSSIBLE"


# def get_jumps(coord_x, coord_y):

#     current_goals = [
#         (0,  1, [NORTH]),
#         (0, -1, [SOUTH]),
#         (-1,  0, [WEST]),
#         (1, 0, [EAST]),
#     ]

#     # max_x_power = int(math.log(x, 2))
#     # max_y_power = int(math.log(y, 2))

#     i = 1
#     while True:
#         new_goals = []

#         for x, y, path in current_goals:
#             new_goals_part = []

#             pow2 = pow(2, i)

#             if y != coord_y:
#                 if abs(coord_y - y) - abs(coord_y - y - pow2) < 0:
#                     new_goals_part.append((x, y + pow2, path + [NORTH]))

#                 if abs(coord_y - y) - abs(coord_y - y + pow2) < 0:
#                     new_goals_part.append((x, y - pow2, path + [SOUTH]))

#             if x != coord_x:
#                 if abs(coord_x - x) - abs(coord_x - x - pow2) < 0:
#                     new_goals_part.append((x - pow2, y, path + [WEST]))

#                 if abs(coord_x - x) - abs(coord_x - x + pow2) < 0:
#                     new_goals_part.append((x + pow2, y, path + [EAST]))

#             # pprint(new_goals_part)
#             # print("---------")

#             for goal in new_goals_part:
#                 if goal[0] == coord_x and goal[1] == coord_y:
#                     return dir_list_to_str(goal[2])

#             new_goals.extend(new_goals_part)

#         if not new_goals:
#             break

#         # pprint(new_goals)
#         # print("----------------------")

#         current_goals = new_goals

#         i += 1

#         # break

#     return 'IMPOSSIBLE'


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        coord_x, coord_y = map(int, next(finput).strip().split())

        match = get_jumps(coord_x, coord_y)

        print('Case #{}: {}'.format(case_no, match))


if __name__ == '__main__':
    main()
