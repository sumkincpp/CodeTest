import fileinput

import math


def walk(N):
    a, b = 0, 1

    for _ in range(100):
        N - a
        a, b = b, a + b


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        N = int(next(finput).strip())

        print('Case #{}:'.format(case_no))

        if N == 1:
            print("1 1")
            continue

        row = math.floor(math.log(N)/math.log(2))

        total = N

        i = 0
        for i in range(1, row):
            print("{} {}".format(i, 1))
            total -= 1

        # print("row {}".format(row))

        for j in range(0, row):
            print("{} {}".format(i + 1, j + 1))

        total -= pow(2, (row-1))

        # print("add {}".format(row))

        while total > 0:
            i += 1
            print("{} {}".format(i + 1, i + 1))
            total -= 1

        # if i % 2 == 0:
        #     print("1 1")
        # else:
        #     print("1 2")


if __name__ == '__main__':
    main()
