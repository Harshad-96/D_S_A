# # class Solution(object):
# #     def threeSum(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: List[List[int]]
# #         """
# #         ans = []
# #         n = len(nums)
# #         for i in range(n):
# #             for j in range(i+1,n):
# #                 for k in range(j+1,n):
# #                     if (nums[i]+nums[j]+nums[k]) == 0:
# #                         triple = sorted([nums[i],nums[j],nums[k]])
# #                         if triple not in ans:
# #                             ans.append(triple)

                        
# #         return ans
# # Better Solution
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ans = []
#         n = len(nums)
#         for i in range(n):
#             s = set()
#             for j in range(i+1,n):
#                 k = -(nums[i]+nums[j])
#                 if k in s:
#                     temp =sorted([nums[i],nums[j],k])
#                     if temp not in ans:
#                         ans.append(temp)
#                 s.add(nums[j])      
#         return ans
            
# Optimal solution

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add > 0:
                    k -= 1
                elif add < 0:
                    j += 1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return ans
            
        