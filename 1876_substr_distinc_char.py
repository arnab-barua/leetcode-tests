class Solution:
    def countGoodSubstrings(s: str) -> int:
        start = 0
        l = len(s)  #6
        f = 0

        while (start + 3) <= l:
            print(s[start:start+3])
            if len(set(s[start:start+3])) == 3:
                print("F")
                f += 1
            start += 1

        return f
    

    # Driver code
    s = "xyzzaba"
    l = countGoodSubstrings(s)
    print(l)