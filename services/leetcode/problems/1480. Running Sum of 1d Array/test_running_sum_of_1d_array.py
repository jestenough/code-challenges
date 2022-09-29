from solution_running_sum_of_1d_array import runningSum


def test_runningSum():
    assert runningSum([1,2,3,4]) == [1,3,6,10]
    assert runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert runningSum([3,1,2,10,1]) == [3,4,6,16,17]