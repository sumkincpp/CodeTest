import fileinput


def get_nesting(data):

    current_nesting = 0

    result = ""

    for c in data:
        i = int(c)

        if i > current_nesting:
            delta = i - current_nesting
            result += "("*delta
            current_nesting = i
        elif i < current_nesting:
            delta = current_nesting - i
            result += ")"*delta
            current_nesting = i

        result += c

    result += ")"*current_nesting

    return result


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        data = next(finput).strip()

        result = get_nesting(data)

        print('Case #{}: {}'.format(case_no, result))


if __name__ == '__main__':
    main()
