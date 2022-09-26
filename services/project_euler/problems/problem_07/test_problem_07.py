from solution_problem_07 import problem_07


def test_problem_06():
    with open("services/project_euler/problems/problem_07/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_07() == answer
