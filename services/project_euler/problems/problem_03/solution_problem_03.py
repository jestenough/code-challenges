def problem_03():
    i = 2
    n = 600851475143
    while i * i <= n:
        print(i)
        if n % i:
            i += 1
        else:
            n //= i
    return n
