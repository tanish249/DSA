class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits=list(map(int,str(x)))
        h=sum(digits)
        if x%h==0:
          return h
        else:
          return -1