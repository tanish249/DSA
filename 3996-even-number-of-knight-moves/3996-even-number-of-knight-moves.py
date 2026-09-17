class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        h=start[0]+start[1]
        g=target[0]+target[1]
        if h%2==g%2:
            return True
        else:
            return False