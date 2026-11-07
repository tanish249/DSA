class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h=sum(nums)
        g=h%k
        return g