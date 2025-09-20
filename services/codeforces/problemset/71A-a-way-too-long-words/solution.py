n = int(input())
words = [input() for _ in range(n)]

for word in words:
    word_len = len(word)
    if word_len > 10:
        print(f"{word[0]}{word_len-2}{word[-1]}")
    else:
        print(word)
