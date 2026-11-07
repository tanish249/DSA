class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        ans=[]
        h=sum(nums)
        for i in nums:
            for j in str(i):
                ans.append(int(j))
        g=sum(ans)
        return abs(g-h)