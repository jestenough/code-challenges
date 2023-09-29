def fake_bin(x):
    return "".join("0" if int(digit) < 5 else "1" for digit in x)
