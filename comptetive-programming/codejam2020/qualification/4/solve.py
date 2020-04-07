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


def reply_solution(finput, guess):
    guess_str = a_to_s(guess)
    print(guess_str)
    sys.stdout.flush()

    res = next(finput).strip()

    if res != 'Y':
        raise ValueError('GUESSS!! {}'.format(guess_str))


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


def read_range(finput, start, end):
    res = []

    for i in range(start, end):
        print(i)
        sys.stdout.flush()
        try:
            num = int(next(finput))
        except Exception:
            raise ValueError(i)

        res.append(num)

    return res


def read_one(finput, i):
    print(i)
    sys.stdout.flush()
    try:
        num = int(next(finput))
    except Exception:
        raise ValueError(i)

    return num


def solve_b20(finput, test_case, b):

    for case_no in range(1, test_case + 1):
        result = [-1 for _ in range(b)]

        uneq_position = None
        eq_position = None

        remaining_unknown = b

        block_size = 5

        # block iteration count
        block_it = 0
        current_iteration = 0

        while uneq_position is None or eq_position is None:
            start5 = read_range(finput,
                                current_iteration + 1,
                                current_iteration + block_size + 1)
            end5 = read_range(finput,
                              b - current_iteration - block_size + 1,
                              b - current_iteration + 1)

            # if block_size - 1 <= 0:
            #     raise ValueError(str(start5) + " - " + str(end5))

            for i in range(0, block_size):
                if start5[i] != end5[block_size - 1 - i]:
                    uneq_position = current_iteration + i
                else:
                    eq_position = current_iteration + i

            for i in range(0, block_size):
                result[current_iteration + i] = start5[i]
                result[b - current_iteration - block_size + i] = end5[i]

            remaining_unknown -= 2*block_size
            current_iteration += block_size

            if remaining_unknown <= 0:
                break

            # if case_no >= 6 and uneq_position:
            #     raise ValueError(
            #         str(uneq_position) + str(start5) + " - " + str(end5))

            # if case_no >= 6 and block_size != 5:
            #     raise ValueError(
            #         str(uneq_position) + "| " + str(eq_position) + "|" +
            #         str(result) + " - " + str(remaining_unknown) + "- " + str(current_iteration))

            # Start == End
            if uneq_position is None:
                r = read_one(finput, 1)

                # Whatever it was -> it lands to two cases
                # initial: 11110XXXXXXXXXX01111
                # start, reversed = 11110XXXXXXXXXX01111
                # compl, rev + compl = 00001XXXXXXXXXX10000
                if r == result[0]:
                    pass
                else:
                    result = compl(result)

                # Quantum Entanglement solved!
                if remaining_unknown <= 0:
                    break

            # Start != End at all
            elif eq_position is None:
                r = read_one(finput, uneq_position + 1)

                # Whatever it was -> it lands to two cases
                # initial: 10101XXXXXXXXXX01010
                # start,reversed+compl = 10101XXXXXXXXXX01010
                # compl,reversed = 01010XXXXXXXXXX10101
                if r == result[uneq_position]:
                    pass
                else:
                    result = compl(result)

                # Quantum Entanglement solved!
                if remaining_unknown <= 0:
                    break

            else:
                break

            # We cant save this misshit
            r = read_one(finput, 1)

            block_size = 4

        # if case_no >= 11:
        #     raise ValueError(str(result) + " - " +
        #                      str(current_iteration) + "|" +
        #                      str(current_block_size) + "|" + str(remaining_unknown))

        # if case_no >= 6:
        #     raise ValueError(str(a_to_s(result)) + " - " +
        #                      str(current_iteration) + "|" +
        #                      str(current_block_size) + "|" + str(remaining_unknown))

        while remaining_unknown > 0:
            new_uneq = read_one(finput, uneq_position + 1)
            new_eq = read_one(finput, eq_position + 1)

            if new_uneq == result[uneq_position]:
                if new_eq == result[eq_position]:
                    # same direction
                    # raise ValueError(str(result) + "b" +
                    #                  str(uneq_position) + str(eq_position))
                    pass
                else:
                    # rev + complement
                    result = rev(compl(result))
                    current_iteration = b - current_iteration - remaining_unknown
                    # raise ValueError(str(result) + "ec" +
                    #                     str(uneq_position) + str(eq_position))
                    pass
            else:
                if new_eq == result[eq_position]:
                    # reverse
                    result = rev(result)
                    current_iteration = b - current_iteration - remaining_unknown
                    # raise ValueError(str(result) + "r" +
                    #                  str(uneq_position) + str(eq_position))
                    pass
                else:
                    # complement
                    result = compl(result)
                    # raise ValueError(str(result) + "c" +
                    #                     str(uneq_position) + str(eq_position))
                    pass

            # if case_no >= 6:
            #     raise ValueError(str(a_to_s(result)) + " - " + str(current_iteration) +
            #                      str(uneq_position) + "-" +
            #                      str(eq_position) + "-" +
            #                      str(new_uneq == result[uneq_position]) + str(new_eq == result[eq_position]))

            current_block_size = min(remaining_unknown, 10 - 2)

            end_ = current_iteration + current_block_size + 1

            # if case_no >= 6:
            #     raise ValueError(str(a_to_s(result)) + " - " +
            #                      str(current_iteration) + "|" +
            #                      str(current_block_size) + "|" + str(remaining_unknown))

            startX = read_range(finput,
                                current_iteration + 1,
                                end_)

            # if case_no >= 6:
            #     raise ValueError(str(a_to_s(result)) + " - " +
            #                      str(current_iteration) + "|" +
            #                      str(startX) + "|" +
            #                      str(current_block_size) + "|" + str(remaining_unknown))

            for i in range(0, current_block_size):
                result[current_iteration + i] = startX[i]

            # if end_ >= 21 or case_no >= 2:
            #     raise ValueError(str(result) + " - " +
            #                      str(current_iteration) + "|" +
            #                      str(current_block_size) + "|" + str(remaining_unknown))

            # raise ValueError(str(result) + "c" +
            #                  str(uneq_position) + str(eq_position))

            current_iteration += current_block_size
            remaining_unknown -= current_block_size

        reply_solution(finput, result)


def main():
    finput = fileinput.input()
    t, b = map(int, next(finput).strip().split(' '))

    if b == 10:
        solve_b10(finput, t, b)
    else:
        solve_b20(finput, t, b)


if __name__ == '__main__':
    main()
