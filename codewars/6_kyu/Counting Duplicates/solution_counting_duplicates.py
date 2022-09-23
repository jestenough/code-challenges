def duplicate_count(text):
    lower_letters_list = list(text.lower())
    return len(dict((letter, lower_letters_list.count(letter)) for letter in set(lower_letters_list) if lower_letters_list.count(letter) > 1))
