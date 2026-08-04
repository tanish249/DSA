class Solution:
    def findGCD(self, nums: List[int]) -> int:
        h=max(nums)
        g=min(nums)
        return gcd(h,g)