class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        start = -1
        end = -1
        low = 0
        high = n-1
        ans = []
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                start = mid
                high = mid - 1  
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1 
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        ans.append(start)
        ans.append(end)
        return ans
        
        