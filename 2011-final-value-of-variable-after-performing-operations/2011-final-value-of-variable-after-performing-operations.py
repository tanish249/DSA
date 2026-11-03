class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        n=len(operations)
        val=0
        for i in range(n):
            if operations[i]=="X++" or operations[i]=="++X":
                val +=1
            elif operations[i]=="--X" or operations[i]=="X--":
                val -=1
        return val