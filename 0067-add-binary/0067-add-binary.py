class Solution:
    def addBinary(self, a: str, b: str) -> str:
        h=int(a,2)
        g=int(b,2)
        sum=h+g
        return (bin(sum)[2:])