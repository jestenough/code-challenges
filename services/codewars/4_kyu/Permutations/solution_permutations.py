def permutations(s):
    # import itertools
    # return set((''.join(i) for i in itertools.permutations(s)))
    # -----------------------------------------------------------

    output = {s[0]}

    for i in range(1, len(s)):
        temp_list = set()
        for elem in output:
            for j in range(len(elem)+1):
                temp_list.add(elem[:j]+s[i]+elem[j:])
        output = temp_list
    return output
