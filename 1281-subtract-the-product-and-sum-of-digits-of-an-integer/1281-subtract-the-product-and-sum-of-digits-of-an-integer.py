import math 

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        h=list(map(int,str(n)))
        g=sum(h)
        f=(math.prod(h))
        return f-g
        