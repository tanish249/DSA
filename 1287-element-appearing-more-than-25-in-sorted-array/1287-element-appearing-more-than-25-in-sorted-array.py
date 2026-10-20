class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        h=max(arr,key=arr.count)
        return h
        