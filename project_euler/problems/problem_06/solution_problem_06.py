def problem_06():
    return sum(range(1,101)) ** 2 - sum((x*x for x in range(1, 101)))
