def problem_07():
    number = 3
    number_of_prime = 2
    while number_of_prime != 10001:
        number += 1
        if is_prime(number):
            number_of_prime += 1
    return number


def is_prime(n):
    if n % 2 == 0:
        return False

    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i += 2
    return True
