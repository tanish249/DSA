class Solution:
    def minimumSum(self, num: int) -> int:
        h=list(map(int,str(num)))
        h.sort()
        num=list(map(str,h))
        o=int(num[0]+num[-1])
        p=int(num[1]+num[2])
        return o+p