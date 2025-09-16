class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        i, n = 0, len(s)

        sign = 1
        if s[i] in "-+":
            if s[i] == "-":
                sign = -1
            i += 1

        output = ""
        while i < n and s[i].isdigit():
            if output or s[i] != "0":
                output += s[i]
            i += 1

        if not output:
            return 0

        n = int(output) * sign

        INT32_MIN = -2**31
        if n < INT32_MIN:
            return INT32_MIN

        INT32_MAX =  2**31 - 1
        if n > INT32_MAX:
            return INT32_MAX

        return n