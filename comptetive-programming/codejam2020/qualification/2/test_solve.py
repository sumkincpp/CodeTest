import solve
import pytest


@pytest.mark.parametrize('data,expected', [
    ["0000", "0000"],
    ["101", "(1)0(1)"],
    ["111000", "(111)000"],
    ["1", "(1)"]
])
def test_calc_subset(data, expected):
    assert solve.get_nesting(data) == expected
