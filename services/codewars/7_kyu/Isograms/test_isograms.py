from solution_isograms import is_isogram


def test_is_isogram():
    assert is_isogram("Dermatoglyphics") == True
    assert is_isogram("isogram") == True
    assert is_isogram("aba") == False
    assert is_isogram("moOse") == False
    assert is_isogram("isIsogram") == False
    assert is_isogram("") == True
