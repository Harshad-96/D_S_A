# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         hashmap = {}
#         for num in nums:
#             if num in hashmap:
#                 hashmap[num] += 1
#             else :
#                 hashmap[num] = 1
#         return max(hashmap,key=hashmap.get)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1 
        return candidate       