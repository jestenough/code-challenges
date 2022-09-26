def problem_08():
    with open("services/project_euler/problems/problem_08/number.txt", 'r') as f:
        number_1000_digit = f.read()

    number_1000_digit = number_1000_digit.replace('\n', '')
    integers_digits = [int(character) for character in number_1000_digit]

    numbers_subsets = []
    len_number = len(number_1000_digit)
    step = 13
    for i in range(len_number - step + 1):
        if 0 not in integers_digits[i:i+step]:
            numbers_subsets.append(integers_digits[i:i+step])

    multiply_numbers = []
    for i in numbers_subsets:
        multiply = 1
        for j in i:
            multiply *= j
        else:
            multiply_numbers.append(multiply)

    return max(multiply_numbers)
