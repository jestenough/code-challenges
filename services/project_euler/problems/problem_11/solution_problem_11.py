def problem_11():
    import os
    with open(os.path.join(os.path.dirname(__file__), 'number.txt'), 'r') as f:
        numbers = f.readlines()

    array = []
    for i in numbers:
        x = i.replace("\n", "")
        array.append(x.split(" "))

    products = []
    for i in range(20):
        for j in range(20):
            k = 0
            right_4, down_4, diagonally_left_4, diagonally_right_4 = 1, 1, 1, 1
            while k != 4:
                if j + k < 20:
                    right_4 *= int(array[i][j+k])

                if i + k < 20:
                    down_4 *= int(array[i+k][j])

                if j - k >= 0 and i + k < 20:
                    diagonally_left_4 *= int(array[j-k][i+k])

                if i + k < 20 and j + k < 20:
                    diagonally_right_4 *= int(array[i+k][j+k])

                k += 1

            products.extend([right_4, down_4, diagonally_left_4, diagonally_right_4])

    return max(products)