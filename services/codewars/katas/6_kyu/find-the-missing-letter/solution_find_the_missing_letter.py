def find_missing_letter(chars):
    alph = set(chr(value) for value in range(ord(chars[0]), ord(chars[-1]) + 1))
    return (alph - set(chars)).pop()
