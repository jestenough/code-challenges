def get_count(sentence):
    return sum(1 for character in sentence if character in ('a', 'e', 'i', 'o', 'u'))
