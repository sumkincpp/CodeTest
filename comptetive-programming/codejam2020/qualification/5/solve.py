import fileinput
import sys
import math


def print_matrix(m):
    for r in m:
        print(" ".join(map(str, r)))


def calc_latin(size, trace):
    diag_elem = trace // size

    # odd and even size matrixes
    if diag_elem * size == trace:
        return latin_diagonal(size, diag_elem)

    if size % 2 == 1:
        return False

    return calc_even(size, trace)


def latin_spec_generator(size, except_vals):
    for i in range(size):
        if (i + 1) in except_vals:
            continue

        yield (i + 1)


def calc_even(size, trace):
    e_min, e_max = 1, size

    if size <= 2:
        return False

    if trace % 2 == 1:
        return False

    base = int(math.floor((trace - 0.5)/size))
    add = (trace - (size - 2) * base) // 2

    if base < e_min or base > e_max:
        return False

    m = [[0]*size for i in range(size)]

    for i in range(size - 2):
        m[i][i] = base
        m[size - 2 - i - 1][i] = add

    m[size - 2][size - 2] = add
    m[size - 1][size - 1] = add
    m[size - 2][size - 1] = base
    m[size - 1][size - 2] = base

    existing_shift = 0

    for i, num in zip(range(1, size + 3),
                      latin_spec_generator(size, [base, add])):

        if m[i][0] and i % 2 == 1:
            existing_shift = 2

        for j in range(size):
            if i % 2 == 0:
                m[(i+j) % size][j] = num
            else:
                m[(i - j + existing_shift) % size][j] = num

    return m


def latin_diagonal(size, diag_elem):
    m = [[0]*size for i in range(size)]

    for i in range(size):
        for j in range(size):
            m[i][(i + j) % size] = (diag_elem - 1 + j) % size + 1
    return m


def main():
    finput = fileinput.input()
    cases, = map(int, next(finput).strip().split(' '))

    for case_no in range(1, cases + 1):
        size, trace = map(int, next(finput).strip().split(' '))

        m = calc_latin(size, trace)

        if m:
            print("Case {}: POSSIBLE".format(case_no))
            print_matrix(m)
        else:
            print("Case {}: IMPOSSIBLE".format(case_no))


if __name__ == '__main__':
    main()
