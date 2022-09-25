def problem_05():
    # * OPTIMIZE ME
    n = 2520
    i = 11
    while i < 21:
        if n % i == 0:
            i += 1
        else:
            i = 11
            n += 20
    return n
