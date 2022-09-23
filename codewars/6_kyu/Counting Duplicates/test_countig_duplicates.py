from solution_counting_duplicates import duplicate_count

def test_duplicate_count():
    assert(duplicate_count("") == 0)
    assert(duplicate_count("abcde") == 0)
    assert(duplicate_count("abcdeaa") == 1)
    assert(duplicate_count("abcdeaB") == 2)
    assert(duplicate_count("Indivisibilities") == 2)
