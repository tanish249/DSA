class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h=list(sorted(s))
        g=list(sorted(t))
        if h==g:
            return True
        else:
            return False