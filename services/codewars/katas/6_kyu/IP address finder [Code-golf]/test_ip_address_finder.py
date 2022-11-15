import os

from solution_ip_address_finder import f


def test_f():
    with open(os.path.join(os.path.dirname(__file__), 'solution_ip_address_finder.py'), 'r') as file:
        text_of_solution = file.read()
    assert text_of_solution.find('import') == -1
    assert len(text_of_solution) <= 59
    assert f("www.codewars.com") == [88, 176, 8, 96]
    assert f("www.starwiki.com") == [110, 220, 74, 184]
