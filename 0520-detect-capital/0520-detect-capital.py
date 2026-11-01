class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        h=word.upper()
        g=word.lower()
        word1=word[0]
        word2=word[1:]
        if h==word or g==word or (word1==word1.upper() and word2==word2.lower()):
            return True
        else:
            return False