class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        h=arrivalTime+delayedTime
        if 24>h:
            return h
        else:
            return h%24