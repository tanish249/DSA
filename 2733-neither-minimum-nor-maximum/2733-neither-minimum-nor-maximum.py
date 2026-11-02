class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        p=nums[n//2]
        if len(nums)>2:
            return p
        else:
            return -1