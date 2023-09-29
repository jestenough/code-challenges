def to_camel_case(text):
    import re
    list_of_words = re.split(r"\-|_", text)
    return list_of_words[0] + "".join([i.title() for i in list_of_words[1:]])