class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        h=list(map(int,str(n)))
        if x in h and h[0]!=x:
            return True
        else:
            return False