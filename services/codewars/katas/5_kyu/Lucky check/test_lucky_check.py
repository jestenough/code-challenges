from sulution_lucky_check import luck_check


def test_luck_check():
    assert luck_check('683179') == True
    assert luck_check('683000') == False