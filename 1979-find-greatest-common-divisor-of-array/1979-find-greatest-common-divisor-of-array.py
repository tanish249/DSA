class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        h=nums[0]
        g=nums[-1]
        return gcd(h,g)