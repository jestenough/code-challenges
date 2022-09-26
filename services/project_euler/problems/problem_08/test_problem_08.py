from solution_problem_08 import problem_08


def test_problem_08():
    with open("services/project_euler/problems/problem_08/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_08() == answer
