def anagrams(word, words):
    output = []
    for i in words:
        if not len(word) == len(i):
            continue
        for j in set(word):
            if not word.count(j) == i.count(j):
                break
        else:
            output.append(i)
    return output
