def snail(snail_map):
    output = []

    while snail_map:
        output.append(get_first_row(snail_map))

        if snail_map:
            output.append(get_right_column(snail_map))
            output.append(get_last_row(snail_map))
            output.append(get_left_column(snail_map))

    return [digit for list_of_digits in output for digit in list_of_digits]


def get_first_row(map) -> list:
    """
    Retrieves the first row (also deleting it in the array of maps)

    Args:
        map: array of arrays

    Returns:
        List of elements of the first row of the array map
    """
    return [*map.pop(0)]


def get_right_column(map) -> list:
    """
    Retrieves the each last element in every array of arrays (also deleting it in the array of maps)

    Args:
        map: array of arrays

    Returns:
        Reverse ('cause the values need to be taken clockwise) list of last elements of each row of the array map
    """
    return [j.pop(-1) for i, j in enumerate(map[:-1])]


def get_left_column(map) -> list:
    """
    Retrieves the each first element in every array of arrays (also deleting it in the array of maps)

    Args:
        map: array of arrays

    Returns:
        Reverse ('cause the values need to be taken clockwise) list of first elements of each row of the array map
    """
    return [j.pop(0) for i, j in enumerate(map[::-1])]


def get_last_row(map) -> list:
    """
    Retrieves the last row (also deleting it in the array of maps)

    Args:
        map: array of arrays

    Returns:
        List of elements of the last row of the array map
    """
    return [*map.pop(-1)][::-1]
