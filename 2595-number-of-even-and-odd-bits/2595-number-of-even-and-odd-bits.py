class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        b=(bin(n)[2:])
        h=b[::-1]
        nums=list(map(int,str(h)))
        n=len(nums)
        ans=[]
        even=0
        odd=0
        for i in range(n):
            if nums[i]==1:
                ans.append(i)
        for i in range(len(ans)):
            if ans[i]%2==0:
                even +=1
            elif ans[i]%2!=0:
                odd +=1
        opp=[even,odd]
        return opp