from solution_problem_16 import problem_16


def test_problem_16():
    with open("services/project_euler/problems/problem_16/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_16() == answer