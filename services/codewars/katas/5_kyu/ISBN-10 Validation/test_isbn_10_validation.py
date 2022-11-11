from solution_isbn_10_validation import valid_ISBN10


def test_valid_ISBN10():
    assert valid_ISBN10('1112223339') == True
    assert valid_ISBN10('048665088X') == True
    assert valid_ISBN10('1293000000') == True
    assert valid_ISBN10('1234554321') == True
    assert valid_ISBN10('1234512345') == False
    assert valid_ISBN10('1293') == False
    assert valid_ISBN10('X123456788') == False
    assert valid_ISBN10('ABCDEFGHIJ') == False
    assert valid_ISBN10('XXXXXXXXXX') == False
    assert valid_ISBN10('123456789T') == False