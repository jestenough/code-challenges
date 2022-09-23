from solution_sum_a_list_buy_ignore_any_duplicates import sum_no_duplicates


def test_sum_no_duplicates():
    assert(sum_no_duplicates([1, 1, 2, 3]) == 5)
    assert(sum_no_duplicates([1, 1, 2, 2, 3]) == 3)
