def move_zeros(lst):
    [lst.append(lst.pop(lst.index(num))) for num in lst if num == 0]
    return lst