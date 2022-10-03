def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return True

    temp = 0
    for i in t:
        if s[temp] == i:
            temp += 1
            if temp == len(s):
                return True
    return False