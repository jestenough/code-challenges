from solution_problem_02 import problem_02


def test_problem_2():
    with open("services/project_euler/problems/problem_02/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_02() == answer
