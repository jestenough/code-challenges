from solution_problem_09 import problem_09


def test_problem_09():
    with open("services/project_euler/problems/problem_09/answer.txt", 'r') as f:
        answer = int(f.read())
    assert problem_09() == answer
