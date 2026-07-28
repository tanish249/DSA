class Solution:
    def removeDuplicates(self, nums):
        temp = []

        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])

        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)