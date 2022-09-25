from solution_problem_04 import problem_04


def test_problem_04():
    with open("services/project_euler/problems/problem_04/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_04() == answer
