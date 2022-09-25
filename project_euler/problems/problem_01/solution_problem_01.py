def problem_01():
    x = sum(i for i in range(0, 1000, 3))
    y = sum(i for i in range(0, 1000, 5))
    z = sum(i for i in range(0, 1000, 15))
    return x + y - z
