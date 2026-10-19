class Solution:
    def hammingWeight(self, n: int) -> int:
        h=(bin(n)[2:])
        g=h.count("1")
        return g