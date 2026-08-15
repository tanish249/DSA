class Solution:
    def isPalindrome(self, x: int) -> bool:
        h=str(x)
        g=h[::-1]
        if h==g:
            return True
        else:
            return False