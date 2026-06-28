class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max1 = 0
        max2 = 0
        for i in range(0,n):
            if nums[i] != 0 :
                max1 += 1
            elif nums[i] == 0:
                if max1 > max2 :
                    max2 = max1
                max1 = 0
        if max1> max2 :
            max2 = max1             
        return(max2)  