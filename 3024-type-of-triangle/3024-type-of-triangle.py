class Solution:
    def triangleType(self, nums: List[int]) -> str:
        f=nums[0]
        g=nums[1]
        h=nums[2]
        if h>=g+f or f>=h+g or g>=f+h:
            return "none"
        elif g+f>h and g+h>f and h+f>g and h==g and g==f and h==f:
            return "equilateral"
        elif g+f>h and g+h>f and h+f>g and h!=g and f!=g and h!=f:
            return "scalene"
        else:
            return "isosceles"