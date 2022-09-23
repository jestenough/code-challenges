def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while (i <= num ** 0.5):
        if num % i == 0:
            return False
        i += 1

    return True
