class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atMost(goal):
            n = len(nums)
            l = 0
            summ = 0
            count = 0
            if goal < 0:
                return 0
            for r in range(n):
                summ += nums[r]
                while summ > goal:
                    summ -= nums[l]
                    l += 1
                count += r - l + 1
            return count

        return atMost(goal) - atMost(goal - 1)