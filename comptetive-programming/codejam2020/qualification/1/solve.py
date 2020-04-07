import fileinput


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        N = int(next(finput).strip())

        m = [map(int, next(finput).strip().split(' ')) for _ in range(N)]

        trace = sum(m[i][i] for i in range(N))

        # r
        collision_rows = 0

        # print(m)

        for i in range(N):
            row = m[i]

            j = 0
            for j in range(N):
                idx = abs(row[j]) - 1

                if row[idx] > 0:
                    row[idx] = - row[idx]
                else:
                    collision_rows += 1
                    break

            # state recovery, only those that we've touched
            for j2 in range(j + 1):
                idx = abs(row[j2]) - 1
                m[i][idx] = abs(m[i][idx])

        # c
        collision_cols = 0

        for j in range(N):
            for i in range(N):
                idx = abs(m[i][j]) - 1

                if m[idx][j] > 0:
                    m[idx][j] = -m[idx][j]
                else:
                    # state recovery not needed

                    collision_cols += 1
                    break

        print('Case #{}: {} {} {}'.format(case_no,
                                          trace,
                                          collision_rows,
                                          collision_cols))


if __name__ == '__main__':
    main()
