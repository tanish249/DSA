class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        h=(bin(a)[2:])
        g=(bin(b)[2:])
        s1=h.count("1")
        s2=g.count("1")
        if s1>=s2:
            return s1*s2
        else:
            return s2//s1