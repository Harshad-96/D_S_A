class Solution(object):
    def sum_posible(self,nums,mid,k):
        n = len(nums)
        inte = 1
        summ = 0
        for i in range(n):
            if summ + nums[i] > mid:
                inte += 1
                summ = nums[i]
            else:
                summ += nums[i]
        if inte > k:
            return False
        else:
            return True
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high)//2
            if self.sum_posible(nums,mid,k):
                high = mid - 1
            else:
                low = mid + 1
        return low
        