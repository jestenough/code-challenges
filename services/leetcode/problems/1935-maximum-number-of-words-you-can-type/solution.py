class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split(" "):
            for broken_letter in brokenLetters:
                if word.find(broken_letter) != -1:
                    break
            else:
                count += 1

        return count
