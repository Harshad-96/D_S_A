class Solution:
    def canplase(self,nums,dist,k):
        cow = nums[0]
        count = 1
        for num in nums:
            if num - cow >= dist:
                count += 1
                cow = num
        if count >= k:
            return True
        else:
            return False

    def aggressiveCows(self, nums, k):
        nums.sort()
        low = 1
        high = max(nums) - min(nums)
        while low <= high:
            mid = (low+high)//2
            if self.canplase(nums,mid,k):
                low = mid + 1
            else:
                high = mid - 1
        return high
        