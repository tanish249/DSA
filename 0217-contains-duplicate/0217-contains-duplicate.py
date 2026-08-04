from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = len(nums)
        g = len(set(nums))
        if h == g:
            return False
        else:
            return True