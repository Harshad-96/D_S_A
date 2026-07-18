class Solution:
    def leaders(self, nums):
        ans = []
        n = len(nums)
        maxi = 0
        for i in range(n-1,-1,-1):
            if maxi < nums[i]:
                ans.append(nums[i])
                maxi = nums[i]
        nums.reverse()
        return ans
        