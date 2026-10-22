class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans1=[]
        ans2=[]
        for i in range(0,n):
            if nums[i]%2==0:
                ans1.append(nums[i])
            else:
                ans2.append(nums[i])
        return ans1+ans2