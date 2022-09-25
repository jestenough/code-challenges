from solution_problem_01 import problem_01


def test_problem1():
    with open('services/project_euler/problems/problem_01/answer.txt', 'r') as f:
        answer = int(f.read())
    assert problem_01() == answer
