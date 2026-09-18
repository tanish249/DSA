class Solution:
    def mirrorDistance(self, n: int) -> int:
        h=str(n)
        g=h[::-1]
        p=int(g)
        return abs(n-p)