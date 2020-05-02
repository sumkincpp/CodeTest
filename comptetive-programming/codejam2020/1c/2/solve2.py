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

    for case_no in range(1, cases + 1):
        radix_buckets = {}

        for i in range(0, 10):
            radix_buckets[i] = {}

        upper_bound = int(next(finput).strip())

        for n_um in range(0, 10000):
            Q_i, coded_value = next(finput).strip().split(' ')

            if Q_i == "-1":
                continue

            max_iteration = len(coded_value)

            # # HIGHEST radix/digit is bad
            if max_iteration == len(Q_i):
                if Q_i[0] != "9":
                    max_iteration -= 1

            for j in range(0, max_iteration):
                last_val = coded_value[-j - 1]
                digit = int(Q_i[-j - 1])

                radix_buckets[digit].setdefault(last_val, 0)
                radix_buckets[digit][last_val] += 1

        num_letter = []

        for i in range(1, 10):
            data = radix_buckets[i]
            # Skipping already known
            for l in num_letter:
                if l in data:
                    del data[l]

            sorted_items = sorted(list(data.items()), key=lambda x: x[1], reverse=True)

            # print(sorted_items)

            num_letter.append(sorted_items[0][0])

        first_letter_set = set(radix_buckets[0].keys()) - set(num_letter)

        num_letter = list(first_letter_set) + num_letter

        coded_value = "".join(num_letter)

        print('Case #{}: {}'.format(case_no, coded_value))


if __name__ == '__main__':
    main()
