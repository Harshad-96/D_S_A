class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            n = len(nums)
            l = 0
            summ = 0
            count = 0
            if k < 0:
                return 0
            for r in range(n):
                summ += (nums[r] % 2)
                while summ > k:
                    summ -= (nums[l] % 2)
                    l += 1
                count += r - l + 1
            return count

        return atMost(k) - atMost(k - 1)
