class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        h=nums[n//2]
        g=nums.count(h)
        if g==1:
            return True
        else:
            return False