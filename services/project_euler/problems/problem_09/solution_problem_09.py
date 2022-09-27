def problem_09():
    # m > n
    # a=m^2-n^2, b=2mn, c=m^2+n^2

    for m in range(1, 100):
        for n in range(m):
            a = m*m - n*n
            b = 2 * m * n
            c = m*m + n*n
            if (a + b + c) == 1000:
                return a * b * c
