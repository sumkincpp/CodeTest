import solve


def test_get_max_move():
    assert solve.get_max_move('P', 'R') == 'P'
    assert solve.get_max_move('P', 'S') == 'S'
    assert solve.get_max_move('P', 'P') == 'S'
    assert solve.get_max_move('R', 'S') == 'R'
