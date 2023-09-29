from solution_find_the_missing_letter import find_missing_letter


def test_find_missing_letter():
    assert find_missing_letter(['a','b','c','d','f']) == 'e'
    assert find_missing_letter(['O','Q','R','S']) == 'P'