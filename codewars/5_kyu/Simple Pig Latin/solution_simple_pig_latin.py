def pig_it(text):
    output = []
    for word in text.split():
        if word.isalpha():
            output.append(f"{word[1:]+word[0]}ay")
        else:
            output.append(word)
    return " ".join(output)
