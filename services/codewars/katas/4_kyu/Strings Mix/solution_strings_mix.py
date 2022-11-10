def mix(s1, s2):
    s1_set = set(z for z in s1 if z.islower())
    s2_set = set(z for z in s2 if z.islower())

    union_of_sets = s1_set.union(s2_set)

    out_list = []
    for value in union_of_sets:
        s1_value = s1.count(value)
        s2_value = s2.count(value)
        if s1_value > 1 or s2_value > 1:
            if s2_value > s1_value:
                out_list.append("2:" + value*s2_value)
            elif s2_value == s1_value:
                out_list.append('=:' + value*s2_value)
            else:
                out_list.append("1:" + value*s1_value)
    else:
        return "/".join(sorted(out_list, key=lambda x: (-len(x), x)))