def encrypt_this(text):
    encrypt_list = []
    for word in text.split():
        list_characters = list(word)
        list_characters[0] = str(ord(list_characters[0]))
        if len(list_characters) > 2:
            list_characters[-1], list_characters[1] = list_characters[1], list_characters[-1]
        encrypt_list.append("".join(list_characters))
    return " ".join(encrypt_list)
