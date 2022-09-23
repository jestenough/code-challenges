from solution_is_a_number_prime import is_prime


def test_is_prime():
    assert(is_prime(0) == False)
    assert(is_prime(1) ==  False)
    assert(is_prime(2) == True)
    assert(is_prime(73) == True)
    assert(is_prime(75) == False)
    assert(is_prime(-1) == False)
