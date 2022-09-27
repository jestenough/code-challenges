from solution_problem_10 import problem_10


def test_problem_10():
    with open("services/project_euler/problems/problem_10/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_10() == answer
