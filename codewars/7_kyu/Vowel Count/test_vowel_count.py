from solution_vowel_count import get_count


def test_get_count():
    assert get_count("aeiou") == 5
    assert get_count("y") == 0
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0
    assert get_count("") == 0
    assert get_count("abracadabra") == 5
