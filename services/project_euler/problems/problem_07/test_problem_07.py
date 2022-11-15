import os

from solution_problem_07 import problem_07


def test_problem_06():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_07() == answer
