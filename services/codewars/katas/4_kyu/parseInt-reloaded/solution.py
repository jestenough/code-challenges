MAPPING = {
    "zero": 0,
    "one": 1,  "two": 2,   "three": 3,  "four": 4,  "five": 5,
    "six": 6,  "seven": 7, "eight": 8,  "nine": 9,  "ten": 10,
    "eleven": 11,  "twelve": 12,  "thirteen": 13,  "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}

SCALES = {
    "hundred": 100,
    "thousand": 1_000,
    "million": 1_000_000,
}

def parse_int(text: str) -> int:
    total = 0
    group = 0  # текущая группа до scale (<= 999)

    for i in text.strip().split():
        if i == "and":
            continue

        if i == "hundred":
            group = max(1, group) * SCALES.get(i)
        elif i in ("thousand", "million"):
            total += max(1, group) * SCALES.get(i)
            group = 0
        elif "-" in i:
            group += sum(MAPPING.get(j) for j in i.split("-"))
        else:
            group += MAPPING.get(i)

    return total + group
