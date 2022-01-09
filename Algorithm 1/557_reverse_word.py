class Solution:
    def reverseWords(s: str) -> str:
        words = s.split(" ")
        for r in range(0, len(words)):
            word = words[r]
            words[r] = word[::-1]

        return " ".join(words)

    s = "God Ding"
    n = reverseWords(s)
    print(n)