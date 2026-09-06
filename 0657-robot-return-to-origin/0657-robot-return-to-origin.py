class Solution:
    def judgeCircle(self, moves: str) -> bool:
        q=moves.count("U")
        w=moves.count("D")
        e=moves.count("R")
        r=moves.count("L")
        if q==w and e==r:
            return True
        else:
            return False