class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                h=nums2[j]-nums1[i]
                ans.append(h)
        return ans[0]