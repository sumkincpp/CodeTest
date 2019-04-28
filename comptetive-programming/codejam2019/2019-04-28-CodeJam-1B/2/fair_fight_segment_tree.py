import fileinput
import math

import unittest


def avg(l, r):
    return (l + r) // 2


class MaxSegmentTree(object):

    def __init__(self, data):
        self.n = len(data)
        #print('{}'.format(math.ceil(math.log(len(data), 2))**2))
        self.st = [None] * (int(2**math.ceil(math.log(len(data), 2))) * 2 - 1)
        #print(self.st)

        #print(len(data))
        #print(len(self.st))
        self.construct(data, 0, len(data)-1)

    def construct(self, data, l, r, curr=0):
        if l == r:
            #print(f"l={l} r={r} data={data} curr={curr}")
            self.st[curr] = data[l]
            return self.st[curr]

        middle = avg(l, r)

        self.st[curr] = max(
            self.construct(data, l, middle, curr*2 + 1),
            self.construct(data, middle+1, r, curr*2 + 2)
        )
        #print(f"l={l} r={r} curr={curr} max={self.st[curr]}")

        return self.st[curr]

    def query(self, ql, qr):
        #print(f"query: ql={ql} qr={qr}")
        return self.__query(ql, qr, 0, self.n-1)

    def __query(self, ql, qr, curr_l, curr_r, curr=0):
        #print(f" __query: ql={ql} qr={qr} l={curr_l} r={curr_r} curr={curr}")
        if ql <= curr_l and qr >= curr_r:
            #print(f" MAX={self.st[curr]}")
            return self.st[curr]

        if curr_r < ql or curr_l > qr:
            return None

        middle = avg(curr_l, curr_r)

        max_1 = self.__query(ql, qr, curr_l, middle, curr*2 + 1)
        max_2 = self.__query(ql, qr, middle+1, curr_r, curr*2 + 2)

        if max_1 is None:
            return max_2

        if max_2 is None:
            return max_1

        return max(max_1, max_2)


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        N, K = map(int, next(finput).strip().split(' '))

        C = list(map(int, next(finput).strip().split(' ')))
        D = list(map(int, next(finput).strip().split(' ')))

        #print(f"C={C}")

        stC = MaxSegmentTree(C)
        stD = MaxSegmentTree(D)

        fair_fights = 0

        for l in range(0, N):
            for r in range(l, N):
                # print("---------------------")
                # print(C)
                # print(stC.st)
                # print(f"l={l} r={r}")
                c_max = stC.query(l, r)
                d_max = stD.query(l, r)

                # print(f"c_max={c_max} d_max={d_max}")

                if abs(c_max - d_max) <= K:
                    fair_fights += 1

        print("Case #{}: {}".format(case_no, fair_fights))


if __name__ == '__main__':
    main()
