class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = "{0:b}".format(n)
        s = s.replace("0","p")
        s = s.replace("1","0")
        s = s.replace("p","1")
        ot = int(s,2)
        return ot