class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if mid > 0 and arr[mid-1] > arr[mid]:
                high = mid - 1
            elif arr[mid+1] > arr[mid]:
                low = mid + 1
            else:
                return mid
        
        