from solution_problem_15 import problem_15


def test_problem_15():
    with open("services/project_euler/problems/problem_15/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_15() == answer