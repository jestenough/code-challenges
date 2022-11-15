import os

from solution_problem_15 import problem_15


def test_problem_15():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_15() == answer