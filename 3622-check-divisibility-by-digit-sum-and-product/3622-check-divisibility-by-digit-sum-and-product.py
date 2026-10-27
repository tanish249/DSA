import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nums=list(map(int,str(n)))
        h=sum(nums)
        g=math.prod(nums)
        p=h+g
        if n%p==0:
            return True
        else:
            return False