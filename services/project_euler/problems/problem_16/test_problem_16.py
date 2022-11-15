import os

from solution_problem_16 import problem_16


def test_problem_16():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_16() == answer