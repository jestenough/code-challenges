def problem_10():
    n = 2_000_000
    A = [i for i in range(n+1)]
    A[1] = 0

    i = 2
    while i <= n:
        if A[i] != 0:
            j = i + i
            while j <= n:
                A[j] = 0
                j = j + i
        i += 1

    return sum(set(A))
