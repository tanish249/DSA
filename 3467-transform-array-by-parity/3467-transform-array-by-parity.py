class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans1=[]
        ans2=[]
        for i in range(0,n):
            if nums[i]%2==0:
                ans1.append(0)
            else:
                ans2.append(1)
        num=ans1+ans2
        num.sort()
        return num