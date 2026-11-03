class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[]
        h=max(nums)
        for i in range(n):
            g=abs(nums[i]-h)
            ans.append(g)
        return sum(ans)
        