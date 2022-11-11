def solution(array_a, array_b):
    return sum((array_b[index] - value) ** 2 for index, value in enumerate(array_a)) / len(array_a)