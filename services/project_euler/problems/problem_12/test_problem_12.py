import os

from solution_problem_12 import problem_12


def test_problem_12():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    # * NOT OPTIMIZED
    # * run time ≈ 2.48 seconds
    # assert problem_12() == answer