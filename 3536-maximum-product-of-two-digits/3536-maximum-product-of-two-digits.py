import math 

class Solution:
    def maxProduct(self, n: int) -> int:
        h=list(map(int,str(n)))
        h.sort()
        o=h[-1]
        p=h[-2]
        return o*p