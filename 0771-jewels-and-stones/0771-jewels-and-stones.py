class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num1=list(jewels)
        num2=list(stones)
        count=0
        for i in num2:
            if i in num1:
                count +=1
        return count

