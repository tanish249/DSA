class Solution:
    def secondHighest(self, s: str) -> int:
        ans1=[]
        ans2=[]
        for i in s:
            if i.isdigit():
                ans1.append(i)
            else:
                ans2.append(i)
        n=len(set(ans1))
        h=list(set(ans1))
        h.sort()
        if n>1:
            return int(h[-2])
        else:
            return -1