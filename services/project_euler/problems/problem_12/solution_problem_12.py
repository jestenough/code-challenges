def problem_12():
    # * NOT OPTIMIZED
    # * run time ≈ 2.48 seconds
    iter_val = 1
    triangle_num = 0
    while True:

        triangle_num += iter_val

        if check_over_500(triangle_num):
            return triangle_num

        iter_val += 1


def check_over_500(n) -> bool:
    temp = 0
    for i in range(1, int((n**0.5))+1):
        if n % i == 0:
            temp += 1
            if n/i != i:
                temp += 1
    return temp >= 500
