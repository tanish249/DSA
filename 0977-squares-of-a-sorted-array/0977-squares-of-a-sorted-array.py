class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in nums:
            ans.append(i**2)
        ans.sort()
        return ans


        