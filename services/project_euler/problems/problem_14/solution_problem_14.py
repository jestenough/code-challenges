def problem_14():
    # * NOT OPTIMIZED
    max_chain = 0
    number = 0
    for i in range(1, 1_000_000):
        chain = 0
        temp = i
        while temp != 1:
            if temp % 2 == 0:
                temp /= 2
            else:
                temp = 3 * temp + 1

            chain += 1

        if max_chain < chain:
            max_chain = chain
            number = i

    return number
