def readints():
    xs = input().split()
    return [int(x) for x in xs]


def get_max_move(a, b):

    win_a = get_win_move(a)

    if a == b:
        return win_a, -1

    win_b = get_win_move(b)

    #print(f"win_a={win_a} win_b={win_b}")

    if win_a == b:
        return b, 1

    if win_b == a:
        return a, 0
#
# def get_res_move(moves):
#     if move == 'P':
#         return set({'P', 'S'})
#     if move == 'R':
#         return set({'P', 'R'})
#     if move == 'S':
#         return set({'S', 'R'})


def get_win_move(move):
    if move == 'P':
        return 'S'
    if move == 'R':
        return 'P'
    if move == 'S':
        return 'R'


# def get_win_move(move):
#     if move == 'P':
#         return set({'P', 'S'})
#     if move == 'R':
#         return set({'P', 'R'})
#     if move == 'S':
#         return set({'S', 'R'})


def main():
    cases = int(input())

    for case_no in range(1, cases+1):
        A = int(input().strip())

        moves_to_win = []

        robots = [list(input().strip()) for adv in range(0, A)]

        i = 0

        is_impossible = False

        while True:
            #print(robots)
            curr_moves = list(set(r[i % len(r)] for r in robots))
            curr_robots = list((r[i % len(r)], r) for r in robots)

            if len(curr_moves) == 3:
                is_impossible = True
                break
            elif len(curr_moves) == 2:
                max_move, remainder = get_max_move(curr_moves[0], curr_moves[1])

                moves_to_win.append(max_move)

                if remainder == -1:
                    break
                elif remainder == 0:
                    robots = [r for move, r in curr_robots if move != curr_moves[1]]
                else:
                    robots = [r for move, r in curr_robots if move != curr_moves[0]]

            else:
                moves_to_win.append(get_win_move(curr_moves[0]))
                break
            i += 1

        if is_impossible:
            print("Case #{}: IMPOSSIBLE".format(case_no))
        else:
            print("Case #{}: {}".format(case_no, ''.join(moves_to_win)))


if __name__ == '__main__':
    main()
