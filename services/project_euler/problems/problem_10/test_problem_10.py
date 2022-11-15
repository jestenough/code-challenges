import os

from solution_problem_10 import problem_10


def test_problem_10():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    assert problem_10() == answer
