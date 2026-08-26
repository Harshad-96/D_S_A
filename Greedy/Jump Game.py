class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxlen = 0
        for i in range(len(nums)):
            if i > maxlen:
                return False
            maxlen = max(maxlen,i+nums[i])
        return True