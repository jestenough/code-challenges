from solution_isomorphic_strings import isIsomorphic


def test_isIsomorphic():
    assert isIsomorphic('egg', 'add') == True
    assert isIsomorphic('foo', 'bar') == False
    assert isIsomorphic('paper', 'title') == True
    assert isIsomorphic('bbbaaaba', 'aaabbbba') == False