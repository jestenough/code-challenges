from solution_pyramid_array import pyramid


def test_pyramid():
    assert pyramid(0) == []
    assert pyramid(1) == [[1]]
    assert pyramid(2) == [[1], [1, 1]]
    assert pyramid(3) == [[1], [1, 1], [1, 1, 1]]