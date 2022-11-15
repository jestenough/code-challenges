import os

from solution_problem_11 import problem_11


def test_problem_11():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_11() == answer
