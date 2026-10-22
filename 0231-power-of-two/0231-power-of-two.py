class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        h=(bin(n)[2:])
        g=h.count("1")
        if g==1 and n>0:
            return True
        else:
            return False