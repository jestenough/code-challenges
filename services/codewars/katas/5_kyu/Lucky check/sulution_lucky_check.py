def luck_check(string):
    if not string.isdigit():
        raise ValueError

    left = sum(map(int, string[:len(string) // 2]))
    right = sum(map(int, string[len(string) // 2 + int(len(string) % 2):]))

    return True if left == right else False