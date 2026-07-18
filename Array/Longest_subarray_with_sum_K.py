class Solution:
    def longestSubarray(self, nums, k):
        
        n = len(nums)
        left = 0
        total = 0
        longest  = 0

        for right in range(n):
            total += nums[right]

            while total > k:
                total -= nums[left]
                left += 1
            
            if k == total:
                longest = max(longest,right-left + 1)
            
        return longest

               