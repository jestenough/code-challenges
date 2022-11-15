import os

from solution_problem_08 import problem_08


def test_problem_08():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_08() == answer
