def wave(people):
    if not people:
        return []

    output_word = []
    for i in range(len(people)):
        if people[i] == ' ':
            continue
        characters = list(people)
        characters[i] = people[i].upper()
        output_word.append("".join(characters))
    return output_word
    