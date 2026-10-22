class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        ans1=[]
        ans2=[]
        for i in nums:
            if 10>i:
                ans1.append(i)
            elif i>=10:
                ans2.append(i)
        h=sum(ans1)
        g=sum(ans2)
        if h!=g:
            return True
        else:
            return False