from solution_problem_11 import problem_11


def test_problem_11():
    with open("services/project_euler/problems/problem_11/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_11() == answer
