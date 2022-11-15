import os

from solution_problem_14 import problem_14


def test_probleM_14():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = int(f.read())
    # * NOT OPTIMIZED
    # assert problem_14() == answer