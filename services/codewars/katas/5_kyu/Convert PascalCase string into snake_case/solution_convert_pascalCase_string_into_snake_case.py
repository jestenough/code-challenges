def to_underscore(string):
    string = str(string)
    output = string[0].lower()
    for letter in string[1:]:
        if letter.isupper():
            output += f"_{letter.lower()}"
        else:
            output += letter
    return output
