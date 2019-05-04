import copy


def readints():
    xs = input().split()
    return [int(x) for x in xs]


def get_poss_moves(cell):
    if cell == 'X':
        return ['V']
    if cell == 'Y':
        return ['H']
    if cell == '.':
        return ['V', 'H']

    return []


def print_t(table):
    print('-----')
    for r in table:
        print(r)


def fill_V_up(table, i, j, R, C):
    k = i

    while k >= 0:
        if table[k][j] == 'H':
            break
        table[k][j] = 'V'

        k -= 1


def fill_V_down(table, i, j, R, C):
    k = i

    while k < R:
        if table[k][j] == 'H':
            break
        table[k][j] = 'V'

        k += 1


def fill_H_left(table, i, j, R, C):
    k = j

    while k >= 0:
        if table[i][k] == 'V':
            break
        table[i][k] = 'H'

        k -= 1


def fill_H_right(table, i, j, R, C):
    k = j

    while k < C:
        if table[i][k] == 'V':
            break
        table[i][k] = 'H'

        k += 1


def get_win_moves(table, R, C, move_count=0):
    win_moves = 0

    no_moves = True

    for i in range(0, R):
        for j in range(0, C):
            moves = get_poss_moves(table[i][j])

            if not moves:
                continue

            no_moves = False

            #print(f"{i} {j} moves={moves}")

            for move in moves:
                #print(f"move={move} move_count={move_count}")
                sub_table = copy.deepcopy(table)

                #print_t(sub_table)

                if move == 'V':
                    #print('filling V')
                    fill_V_up(sub_table, i, j, R, C)
                    fill_V_down(sub_table, i, j, R, C)
                else:
                    #print('filling H')
                    fill_H_right(sub_table, i, j, R, C)
                    fill_H_left(sub_table, i, j, R, C)

                #print_t(sub_table)

                win_moves += get_win_moves(sub_table, R, C, move_count + 1)

    if no_moves:
        #print(f"Full table on move_count={move_count}")
        #print_t(table)
        return move_count % 2
    else:
        if win_moves == 0:
            return win_moves
        if move_count == 0:
            return win_moves

        return 1


def main():
    cases = int(input())

    for case_no in range(1, cases+1):
        R, C = readints()

        table = [list(input().strip()) for r in range(0, R)]

        r_cells_x = []
        r_cells_y = []

        for i in range(0, R):
            for j in range(0, C):
                if table[i][j] == '#':

                    for r in range(0, R):
                        if table[r][j] == '#':
                            continue

                        if table[r][j] == 'X':
                            table[r][j] = 'Z'
                        else:
                            table[r][j] = 'Y'

                    for c in range(0, C):
                        if table[i][c] == '#':
                            continue

                        if table[i][c] == 'Y':
                            table[i][c] = 'Z'
                        else:
                            table[i][c] = 'X'

                    table[i][j] = '#'
                    # r_cells_x.append(i)
                    # r_cells_y.append(j)

        count = get_win_moves(table, R, C)

        # print(r_cells_x)
        # print(r_cells_y)
        # print('-----')
        # for r in table:
        #     print(r)

        print("Case #{}: {}".format(case_no, count))


if __name__ == '__main__':
    main()
