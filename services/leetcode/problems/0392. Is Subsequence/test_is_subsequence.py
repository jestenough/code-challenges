from solution_is_subsequence import isSubsequence


def test_isSubsequence():
    assert isSubsequence('abc', 'ahbgdc') == True
    assert isSubsequence('axc', 'ahbgdc') == False
    assert isSubsequence('', 'ahbgdc') == True
    assert isSubsequence('ace', 'abedc') == False