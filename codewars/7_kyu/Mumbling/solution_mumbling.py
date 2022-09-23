def accum(s):
    return '-'.join([(value * (index+1)).capitalize() for index, value in enumerate(s)])
