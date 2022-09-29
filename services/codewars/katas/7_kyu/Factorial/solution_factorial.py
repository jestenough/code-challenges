def factorial(n):
    if n < 0 or n > 12:
        raise ValueError()
    else:
        return 1 if n == 0 else n * factorial(n - 1)
