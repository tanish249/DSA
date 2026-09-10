class Solution:
    def countCommas(self, n: int) -> int:
        h=abs(1000-n)
        if n>=1000:
            return h+1
        else:
            return 0