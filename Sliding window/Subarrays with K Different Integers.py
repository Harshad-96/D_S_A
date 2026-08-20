class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atMost(nums,k) - self.atMost(nums,k-1)
    def atMost(self, nums, k):
        if k == 0:
            return 0
        l = 0
        dic = {}
        count = 0
        for r in range(len(nums)):
            dic[nums[r]] = dic.get(nums[r], 0) + 1
            
            while len(dic) > k:
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1
            
            count += (r - l + 1)
        return count
        