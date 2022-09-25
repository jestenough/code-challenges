from re import L
from solution_find_the_unique_number import find_uniq


def test_find_uniq():
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10
