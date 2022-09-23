def find_uniq(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i
