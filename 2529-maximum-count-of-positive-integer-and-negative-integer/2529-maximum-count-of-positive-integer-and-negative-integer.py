class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n=len(nums)
        count1=0
        count2=0
        for i in range(n):
            if nums[i]>0:
                count1 +=1
            elif 0>nums[i]:
                count2 +=1
        h=max(count1,count2)
        return h