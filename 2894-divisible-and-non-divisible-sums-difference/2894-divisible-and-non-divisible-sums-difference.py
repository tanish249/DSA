class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans1=[]
        ans2=[]
        for i in range(0,n+1):
            if i%m==0:
                ans1.append(i)
            else:
                ans2.append(i)
        h=sum(ans1)
        g=sum(ans2)
        return g-h