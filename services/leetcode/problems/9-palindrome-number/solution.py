class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            return False

        right = 1
        left = 1
        while x // left >= 10:
            left *= 10

        while left > right:
            if (x // left) % 10 != (x // right) % 10:
                return False
            left //= 10
            right *= 10
        return True