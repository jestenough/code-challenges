def first_non_repeating_letter(string):
    for letter in string:
        if string.lower().count(letter.lower()) == 1:
            return letter
    return ""
