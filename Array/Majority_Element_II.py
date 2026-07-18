# # BruteForce Solution
# # class Solution(object):
# #     def majorityElement(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: List[int]
# #         """
# #         count = 0
# #         ans = []
# #         n = len(nums)
# #         for i in range(n):  
# #             if nums[i] not in ans :
# #                 count = 0
# #                 for j in range(n):
# #                     if nums[i] == nums[j]:
# #                         count +=1
# #                 if count > n/3:
# #                     ans.append(nums[i])
# #         return ans   

# # Better Solution

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         n = len(nums)
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num,0) + 1
#         for num , count in freq.items():
#             if count > n/3 :
#                 ans.append(num)
#         return ans

# Optimal Solution

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        ele1,ele2 = float('-inf'),float('-inf')
        count1 = 0
        count2 = 0
        for i in range(n):
            if count1 == 0 and ele2 != nums[i]:
                ele1 = nums[i]
                count1 += 1
            elif count2 == 0 and ele1 != nums[i]:
                ele2 = nums[i]
                count2 += 1
            elif nums[i] == ele1:
                count1 += 1
            elif nums[i] == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1 
        actual_count1 = 0
        actual_count2 = 0
        for i in range(n):
            if nums[i] == ele1:
                actual_count1 += 1
            if nums[i] == ele2:
                actual_count2 += 1
        if actual_count1 > n/3:
            ans.append(ele1)
        if actual_count2 > n/3:
            ans.append(ele2)
        return ans