def valid_ISBN10(isbn):
    if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')) or len(isbn) != 10:  # REGEX ??? ??
        return False

    return sum(i*(int(j) if j != 'X' else 10) for i, j in enumerate(isbn, 1)) % 11 == 0