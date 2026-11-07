class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        ans1=[]
        ans2=[]
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                ans1.append(i)
            elif nums1[i]%2!=0:
                ans2.append(i)
        h=len(ans1)
        g=len(ans2)
        if h==g or h>g or g>h:
            return True
        else:
            return False