from solution_is_the_string_uppercase import is_uppercase


def test_is_uppercase():
    assert is_uppercase("c") == False
    assert is_uppercase("C") == True
    assert is_uppercase("hello I AM DONALD") == False
    assert is_uppercase("HELLO I AM DONALD") == True
    assert is_uppercase("$%&") == True
