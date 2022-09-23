def is_isogram(string):
    return False if len(set(string.lower())) < len(string.lower()) else True
