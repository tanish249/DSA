class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        g=sorted(set(nums))
        h=len(g)
        if 3>h:
            return max(g)
        else:
            return g[-3]