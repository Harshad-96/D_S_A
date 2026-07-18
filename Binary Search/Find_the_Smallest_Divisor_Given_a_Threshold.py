import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low+high)//2
            if self.deviser(nums,mid,threshold):
                high = mid - 1
            else:
                low = mid + 1
        return low
    def deviser(self,nums,div,threshold):
        summ = 0
        for num in nums:
            summ += math.ceil(num/float(div))
        if summ <= threshold:
            return True
        else:
            return False
        
        