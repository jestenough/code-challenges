from solution_scramblies import scramble


def test_scramble():
    assert(scramble('rkqodlw', 'world') == True)
    assert(scramble('cedewaraaossoqqyt', 'codewars') == True)
    assert(scramble('katas', 'steak') == False)
    assert(scramble('scriptjava', 'javascript') == True)
    assert(scramble('scriptingjava', 'javascript') == True)
