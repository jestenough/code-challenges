from solution_problem_03 import problem_03


def test_problem_03():
    with open('services/project_euler/problems/problem_03/answer.txt', 'r') as f:
        answer = int(f.read())
        assert problem_03() == answer
