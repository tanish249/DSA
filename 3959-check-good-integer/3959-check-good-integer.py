class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        nums=list(map(int,str(n)))
        ans = []
        for i in nums:
            ans.append(i**2)
        h=sum(nums)
        g=sum(ans)
        p=abs(h-g)
        if p>=50:
            return True
        else:
            return False

        