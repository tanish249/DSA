class Solution:
    def countDigits(self, num: int) -> int:
        g=num
        nums=list(map(int,str(g)))
        count =0 
        for i in nums:
            if num%i==0:
                count +=1
        return count
        