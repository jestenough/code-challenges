class Solution:
    def reverse(self, x: int) -> int:
        MAX_32 = 2 ** 31 - 1

        sign = [1, -1][x < 0]
        y, x = 0, abs(x)
        while x > 0:
            y *= 10
            y += x % 10
            if y > MAX_32:
                return 0
            x //= 10

        return y * sign
