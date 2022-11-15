import os

from solution_problem_09 import problem_09


def test_problem_09():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_09() == answer
