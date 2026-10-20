class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        o=list(set(sentence))
        if len(o)==26:
            return True
        else:
            return False

        