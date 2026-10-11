class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        h=nums[n//2]
        f=nums.count(h)
        if f==1:
            return True
        else:
            return False