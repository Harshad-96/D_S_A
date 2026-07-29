class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        subset = 1 << n
        ans = []
        for num in range(subset):
            listt = []
            for i in range(n):
                if num & 1 << i:
                    listt.append(nums[i])
            ans.append(listt)
        return ans