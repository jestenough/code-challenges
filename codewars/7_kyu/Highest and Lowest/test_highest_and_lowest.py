from solution_highest_and_lowest import high_and_low


def test_high_and_low():
    assert(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9");
    assert(high_and_low("1 2 3") == "3 1");
