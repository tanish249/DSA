class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        ans1=nums.copy()
        ans2=nums.copy()
        ans1.sort()
        ans2.sort(reverse=True)
        if nums==ans1 or nums==ans2:
            return True
        else:
            return False
        