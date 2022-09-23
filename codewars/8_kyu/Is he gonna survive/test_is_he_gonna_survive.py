from solution_is_he_gonna_survive import hero


def test_hero():
    assert(hero(10, 5) == True)
    assert(hero(7, 4) == False)
    assert(hero(4, 5) == False)
    assert(hero(100, 40) == True)
    assert(hero(1500, 751) == False)
    assert(hero(0, 1) == False)
