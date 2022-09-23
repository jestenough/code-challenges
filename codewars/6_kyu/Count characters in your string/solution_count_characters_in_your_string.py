def count(string):
    return dict(map(lambda character: (character, string.count(character)), set(string)))
