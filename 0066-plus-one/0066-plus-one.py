class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=int("".join(map(str,digits)))
        h=a+1
        return (list(map(int,str(h))))
