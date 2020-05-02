import fileinput

import math

from pprint import pprint


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

        start_values = set()
        all_values = set()

        for n_um in range(0, 10000):
            Q_i, coded_value = next(finput).strip().split(' ')

            if Q_i == "-1":
                continue

            start_iteration = 0

            start_values.add(coded_value[0])
            all_values.add(coded_value[-1])

            for j in range(start_iteration, len(coded_value)):
                last_val = coded_value[j]
                digit = int(Q_i[j])

                radix_buckets[digit].setdefault(last_val, 0)
                radix_buckets[digit][last_val] += 1

        max_items = []

        for i in range(0, 10):
            data = radix_buckets[i]

            max_item = sorted(list(data.items()), key=lambda x: x[1], reverse=True)

            max_items.append(max_item)

        max_items_sorted = sorted(enumerate(max_items), key=lambda x: x[1][0][1], reverse=True)

        num_letter = []

        for i, data in max_items_sorted[:-2]:
            # Skipping already known
            for l in num_letter:
                for j in range(0, len(data)):
                    if l == data[j][0]:
                        del data[j]
                        break

            letter = data[0][0]

            num_letter.append(letter)

        zero_letter = next(iter(all_values - start_values))
        ninth_letter = next(iter((all_values) - set(num_letter) - set(zero_letter)))

        # print("{} {}".format(zero_letter, ninth_letter))

        # first_letter_set = set(radix_buckets[0].keys()) - set(num_letter)

        # num_letter = list(first_letter_set) + num_letter

        num_letter = [zero_letter] + num_letter + [ninth_letter]

        coded_value = "".join(num_letter)

        print('Case #{}: {}'.format(case_no, coded_value))


if __name__ == '__main__':
    main()
