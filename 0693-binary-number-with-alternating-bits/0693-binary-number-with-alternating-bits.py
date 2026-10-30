class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        h=(bin(n)[2:])
        num=list(map(int,str(h)))
        n=len(num)
        for i in range(0,n-1):
            if num[i]==num[i+1]:
                return False
                break
        else:
                return True
        