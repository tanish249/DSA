class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        h=nums[0]*nums[1]
        g=nums[-1]*nums[-2]
        return abs(h-g)