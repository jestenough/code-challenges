def problem_04():
    max = 0
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            if str(j * i) == str(j * i)[::-1]:
                if max < i * j:
                    max = i * j
    return max
