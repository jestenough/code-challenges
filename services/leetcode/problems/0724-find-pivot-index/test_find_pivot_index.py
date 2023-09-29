from solution_find_pivot_index import pivotIndex


def test_pivotIndex():
    assert pivotIndex([1,7,3,6,5,6]) == 3
    assert pivotIndex([1,2,3]) == -1
    assert pivotIndex([2,1,-1]) == 0