def problem_17():
    ones = {
        0: 0, 1: 3, 2: 3, 3: 5, 4: 4,
        5: 4, 6: 3, 7: 5, 8: 5, 9:4,
        10: 3, 11: 6, 12: 6, 13: 8, 14: 8,
        15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
    }

    tens = {
        0: 0,
        10: 0,
        20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90:6
    }

    count = 0
    for i in range(1, 1000):
        if i < 20:
            count += ones[i]
        elif i < 100:
            count += tens[i // 10 * 10] + ones[i % 10]
        else:
            count += ones[i // 100] + 7
            if i // 10 % 10 >= 2:
                count += tens[i % 100 // 10 * 10] + ones[i % 10]
            else:
                count += ones[i % 100]

            if i % 100 != 0:
                # number of letters for "and"
                # check 'numbers is in compliance with British usage'
                count += 3
    else:
        count += ones[1000 // 1000] + 8

    return count
