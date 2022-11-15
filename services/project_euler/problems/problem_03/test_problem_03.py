import os

from solution_problem_03 import problem_03


def test_problem_03():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
        assert problem_03() == answer
