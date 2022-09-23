def sum_no_duplicates(l):
    return sum([i for i in l if l.count(i) == 1])
