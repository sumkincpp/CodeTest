import fileinput

# from pprint import pprint


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        N = int(next(finput).strip())

        workers = {
            'C': 0,
            'J': 0
        }

        result = [' ']*N

        is_impossible = False

        activities = [map(int, next(finput).strip().split(' '))
                      for _ in range(N)]

        activities = sorted(enumerate(activities), key=lambda x: x[1])

        for order, activity in activities:
            start, end = activity

            is_activity_performed = False

            # ordered_workers = sorted(
            #     workers.keys(), key=lambda x: workers[x], reverse=True)

            # print(workers)
            # print(ordered_workers)

            for w in workers.keys():
                if workers[w] > start:
                    continue

                # Making activity
                workers[w] = end

                result[order] = w
                is_activity_performed = True
                break

            if not is_activity_performed:
                is_impossible = True
                break

        if is_impossible:
            result = "IMPOSSIBLE"

        print('Case #{}: {}'.format(case_no, "".join(result)))


if __name__ == '__main__':
    main()
