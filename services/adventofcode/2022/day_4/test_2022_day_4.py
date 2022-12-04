import os
from solution_2022_day_4 import day_4_two_parts


def test_day_4_two_parts():
    with open(os.path.join(os.path.dirname(__file__), 'answer.txt'), 'r') as f:
        answer = f.read().split("\n")
    assert day_4_two_parts() == [int(answer[0]), int(answer[1])]