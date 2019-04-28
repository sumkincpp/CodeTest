import fileinput


def max_range(data):
    size = len(data)

    table = [[None for i in range(0, size)] for i in range(0, size)]

    for i in range(0, size):
        table[i][i] = data[i]

    # 1,0 2,1 3,2 4,3 5,4
    # 2,0 2,1 2,2 3,2
    for x in range(1, size):
        for y in range(0, size - x):
            table[x+y][y] = max(table[x+y-1][y], table[x+y][y+1])

    return table


def get_max_range(table, l, r):
    if l > r:
        l, r = r, l

    return table[r][l]


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        N, K = map(int, next(finput).strip().split(' '))

        C = list(map(int, next(finput).strip().split(' ')))
        D = list(map(int, next(finput).strip().split(' ')))

        max_table_C = max_range(C)
        max_table_D = max_range(D)

        fair_fights = 0

        for l in range(0, N):
            for r in range(l, N):
                c_max = get_max_range(max_table_C, l, r)
                d_max = get_max_range(max_table_D, l, r)

                if abs(c_max - d_max) <= K:
                    fair_fights += 1

        print("Case #{}: {}".format(case_no, fair_fights))


if __name__ == '__main__':
    main()
