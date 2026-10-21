import math 

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        h=math.prod(nums)
        if h>0:
            return 1
        elif 0>h:
            return -1
        else:
            return 0

        