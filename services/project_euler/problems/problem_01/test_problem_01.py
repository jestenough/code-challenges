import os

from solution_problem_01 import problem_01


def test_problem1():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_01() == answer
