class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        summ = 0
        prev_val = 0
        for num in s[::]:
            val = numerals.get(num)
            if prev_val < val:
                summ += val - prev_val * 2
            else:
                summ += val
            prev_val = val

        return summ