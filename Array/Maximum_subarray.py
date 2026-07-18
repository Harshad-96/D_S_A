class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = nums[0]
        sum = 0
        for num in nums:
            sum += num
            maxi = max(maxi,sum)
            if sum < 0:
                sum = 0
        return maxi
    