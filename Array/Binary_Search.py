# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         n = len(nums)
#         low = 0
#         high = n-1
#         while low <= high:
#             mid = (low + high)//2
#             if nums[mid] == target:
#                 return mid
#             elif target > nums[mid]:
#                 low = mid+1
#             else:
#                 high = mid-1
#         return -1
# By using recursion

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bs(low,high):
            if low > high:
                return -1
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return bs(mid+1,high)
            else:
                return bs(low,mid-1)
        return bs(0,len(nums)-1)
         