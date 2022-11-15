import os

from solution_problem_17 import problem_17


def test_problem_17():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
       answer = int(f.read())
    assert problem_17() == answer