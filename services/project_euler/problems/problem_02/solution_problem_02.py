def problem_02():
    num_1, num_2 = 1, 2
    sum_of_even = 0
    while num_2 < 4_000_000:
        if num_2 % 2 == 0:
            sum_of_even += num_2
        num_1, num_2 = num_2, num_1 + num_2
    return sum_of_even
