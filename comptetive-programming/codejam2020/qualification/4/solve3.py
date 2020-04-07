import fileinput
import sys


def solve_b10(finput, t, b):
    number = [0]*b

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


def arr_startswith(a1, a2):

    for i in range(0, len(a2)):
        if a1[i] != a2[i]:
            return False

    return True


def rev(a):
    return list(reversed(a))


def compl(a):
    return list(1 - i for i in a)


def compl_rev(a):
    return compl(rev(a))


def a_to_s(a):
    return "".join(map(str, a))


def solve_b20(finput, test_case, b):

    for _ in range(1, test_case + 1):
        read_data_list = []
        for t in range(2):
            read_data = {
                'start': [],
                'end': []
            }

            for i in range(0, 3):
                in_number = t * 3 + i + 1
                print(in_number)
                sys.stdout.flush()
                try:
                    num = int(next(finput))
                except Exception:
                    raise ValueError(in_number)

                read_data['start'].append(num)

            for i in range(0, 3):
                in_number = b - (t + 1) * 3 + i + 1
                print(in_number)
                sys.stdout.flush()
                try:
                    num = int(next(finput))
                except Exception:
                    raise ValueError(in_number)

                read_data['end'].append(num)

            read_data_list.append(read_data)

        # guesses = [[] for i in range(4)]

        # guesses[0].extend(read_data_list[0]['start'])
        # guesses[1].extend(rev(read_data_list[0]['end']))
        # guesses[2].extend(compl(read_data_list[0]['start']))
        # guesses[3].extend(compl_rev(read_data_list[0]['end']))

        # for g in guesses:
        #     # g.extend('x'*10)
        #     g.extend(read_data_list[1]['start'] + read_data_list[1]['end'])

        # guesses[0].extend(read_data_list[0]['end'])
        # guesses[1].extend(rev(read_data_list[0]['start']))
        # guesses[2].extend(compl(read_data_list[0]['end']))
        # guesses[3].extend(compl_rev(read_data_list[0]['start']))

        # for g in guesses:
        #     print(a_to_s(g))
        #     sys.stdout.flush()

        #     res = next(finput).strip()

        #     if res == 'Y':
        #         break
        #     else:
        #         continue
        # # guesses = [a_to_s(a) for a in guesses]

        # some_part = []

        # for i in range(0, 9):
        #     in_number = i + 1
        #     print(in_number)
        #     sys.stdout.flush()
        #     try:
        #         num = int(next(finput))
        #     except Exception:
        #         raise ValueError(in_number)

        #     some_part.append(num)

        # for g in guesses:
        #     if arr_startswith(g, some_part):
        #         res = g
        #     elif arr_startswith(g, rev(some_part)):
        #         res = rev(g)
        #     elif arr_startswith(g, compl_rev(some_part)):
        #         res = compl_rev(g)
        #     elif arr_startswith(g, compl(some_part)):
        #         res = compl(g)
        #     else:
        #         continue

        #     print(a_to_s(res))
        #     sys.stdout.flush()

        #     res = next(finput).strip()

        #     if res == 'Y':
        #         break
        #     else:
        #         sys.exit(0)

        # sys.exit(0)

        raise ValueError([a_to_s(g) for g in guesses])


def main():
    finput = fileinput.input()
    t, b = map(int, next(finput).strip().split(' '))

    if b == 10:
        solve_b10(finput, t, b)
    elif b == 20:
        solve_b20(finput, t, b)


if __name__ == '__main__':
    main()
