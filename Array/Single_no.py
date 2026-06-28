class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        xor = 0
        for num in nums:
            xor ^= num
        return xor    

