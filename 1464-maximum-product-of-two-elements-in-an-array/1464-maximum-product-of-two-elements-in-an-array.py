class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        h=nums[-1]-1
        g=nums[-2]-1
        return h*g