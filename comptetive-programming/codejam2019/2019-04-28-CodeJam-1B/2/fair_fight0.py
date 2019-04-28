import fileinput

import heapq


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        N, K = map(int, next(finput).strip().split(' '))

        C = list(map(int, next(finput).strip().split(' ')))
        D = list(map(int, next(finput).strip().split(' ')))

        fair_fights = 0

        for L in range(0, N):
            for R in range(L, N):

                cj = max(C[L:R+1])
                dj = max(D[L:R+1])

                if abs(cj - dj) <= K:
                    fair_fights += 1

        print("Case #{}: {}".format(case_no, fair_fights))


if __name__ == '__main__':
    main()
