def parse(data):
    value = 0
    result = []
    data = (i for i in data if i in 'idso')  # useful for the worst result
    for letter in data:
        match letter:
            case 'i':
                value += 1
            case 'd':
                value -= 1
            case 's':
                value *= value
            case 'o':
                result.append(value)
    return result
