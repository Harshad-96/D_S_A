class Solution:
    def lowerBound(self, nums, x):
        n = len(nums)
        ans = n
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= x:
                high = mid-11
                ans = mid
            else:
                low = mid + 1
        return ans
       


