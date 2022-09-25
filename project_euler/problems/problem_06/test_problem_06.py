from solution_problem_06 import problem_06


def test_problem_06():
    with open("services/project_euler/problems/problem_06/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_06() == answer
