class Solution:
    def findComplement(self, num: int) -> int:
        a=(bin(num)[2:])
        ans=[]
        for i in a:
            if i=="1":
                ans.append(0)
            elif i=="0":
                ans.append(1)
        p="".join(map(str,ans))
        h=int(p,2)
        return h
        
        