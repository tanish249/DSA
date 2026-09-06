class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        h="".join(word1)

        g="".join(word2)

        if h==g:

            return True

        else:

            return False