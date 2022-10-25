from solution_problem_17 import problem_17


def test_problem_17():
    with open("services/project_euler/problems/problem_17/answer.txt", 'r') as f:
       answer = int(f.read())
    assert problem_17() == answer