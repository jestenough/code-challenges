import os

from solution_problem_04 import problem_04


def test_problem_04():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_04() == answer
