def problem_13():
    with open("services/project_euler/problems/problem_13/number.txt", 'r') as f:
        return int(str(sum(int(i) for i in f.readlines()))[:10])
