from solution_mean_square_error import solution


def test_solution():
    a1 = [1,2,3]
    a2 = [4,5,6]
    assert solution(a1, a2) == 9

    b1 = [10, 20, 10, 2]
    b2 = [10, 25, 5, -2]

    assert solution(b1, b2) == 16.5

    c1 = [0, -1]
    c2 = [-1, 0]

    assert solution(c1, c2) == 1

    d1 = [10, 10]
    d2 = [10, 10]

    assert solution(d1, d2) == 0