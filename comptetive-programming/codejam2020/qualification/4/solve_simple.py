import fileinput
import sys


def main():
    finput = fileinput.input()
    t, b = map(int, next(finput).strip().split(' '))

    number = [0]*b

    broken_idxs = []

    for case_no in range(1, t + 1):
        for i in range(0, b):
            print(i + 1)
            sys.stdout.flush()
            num = int(next(finput))
            number[i] = num

            if i % 10 == 0:
                broken_idxs = i

        print("".join(map(str, number)))
        sys.stdout.flush()

        res = next(finput).strip()

        if res == 'Y':
            continue


if __name__ == '__main__':
    main()
