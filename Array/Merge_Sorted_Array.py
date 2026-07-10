# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         a = len(nums1)
#         b = len(nums2)
#         i = 0
#         j = 0
#         ans = []
#         while i < m and j < n:
#             if nums1[i] <= nums2[j]:
#                 ans.append(nums1[i])
#                 i += 1
#             else:
#                 ans.append(nums2[j])
#                 j += 1
#         while j < n:
#             ans.append(nums2[j])
#             j += 1
#         while i < m:
#             ans.append(nums1[i])
#             i += 1
#         for i in range(len(ans)):  
#             nums1[i] = ans[i]
        
# Optimal solution

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

              