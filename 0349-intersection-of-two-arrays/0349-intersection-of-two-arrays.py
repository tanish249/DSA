class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        h=set(nums1)
        g=set(nums2)
        common=[]
        for i in g:
            if i in h:
                common.append(i)
        return common

