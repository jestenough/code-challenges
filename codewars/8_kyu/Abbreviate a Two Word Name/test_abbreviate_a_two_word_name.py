from solution_abbreviate_a_two_word_name import abbrev_name


def test_abbrev_name():
    assert abbrev_name("Sam Harris") == "S.H"
    assert abbrev_name("patrick feenan") == "P.F"
    assert abbrev_name("Evan C") == "E.C"
    assert abbrev_name("P Favuzzi") == "P.F"
    assert abbrev_name("David Mendieta") == "D.M"
