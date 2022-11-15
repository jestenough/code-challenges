import os

from solution_problem_13 import problem_13


def test_problem_13():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_13() == answer