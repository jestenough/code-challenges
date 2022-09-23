from solution_count_characters_in_your_string import count


def test_count():
    assert(count('aba') == {'a': 2, 'b': 1})
    assert(count('') == {})
