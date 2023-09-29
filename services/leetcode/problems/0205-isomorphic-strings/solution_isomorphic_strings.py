def isIsomorphic(s: str, t: str) -> bool:
    for i in range(len(s)):
        if not s.index(s[i]) == t.index(t[i]):
            return False
    else:
        return True