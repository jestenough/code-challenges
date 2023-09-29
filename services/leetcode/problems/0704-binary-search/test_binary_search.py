from solution_binary_search import search


def test_search():
    assert search([-1,0,3,5,9,12], 9) == 4
    assert search([-1,0,3,5,9,12], 2) == -1
    assert search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == 2
    assert search([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 8, 10], -4) == 1
    assert search([0], 0) == 0