class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        h=abs(x-z)
        g=abs(y-z)
        if g>h:
            return 1
        elif h>g:
            return 2
        else:
            return 0