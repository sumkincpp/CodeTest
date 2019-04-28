def readline():
    return input()


def readint():
    return int(input())


def readfloat():
    return float(input())


def readints():
    xs = input().split()
    return [int(x) for x in xs]


def readfloats():
    xs = input().split()
    return [float(x) for x in xs]


def printcase(casenum, x):
    print('Case #{:d}: {}'.format(casenum, x))


def run(main):
    t = readint()
    for casenum in range(1, t + 1):
        main(casenum)


def search(xs, q):
    best = None
    best_val = -9999999

    cur = 0
    cur_val = 0
    for x, s in xs:
        print(f"x={x} s={s} curr={cur} curr_val={cur_val} best={best} best_val={best_val}")
        if x <= cur:
            cur_val += s
        else:
            if cur <= q and cur_val > best_val:
                best = cur
                best_val = cur_val
            cur = x
            cur_val += s

    if cur <= q and cur_val > best_val:
        best = cur
        best_val = cur_val

    return best


def main(casenum):
    p, q = readints()
    xs = []
    ys = []
    for i in range(p):
        a, b, c = readline().split()
        if c == 'N':
            ys.append((int(b) + 1, 1))
        elif c == 'S':
            ys.append((int(b), -1))
        elif c == 'E':
            xs.append((int(a) + 1, 1))
        elif c == 'W':
            xs.append((int(a), -1))

    xs.sort()
    print(f"xs = {xs}")
    x = search(xs, q)

    ys.sort()
    print(f"ys = {ys}")
    y = search(ys, q)
    printcase(casenum, '{} {}'.format(x, y))


run(main)
