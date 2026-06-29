class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i , num in enumerate(nums):
            compare = target - num
            
            if compare in hashmap:
                return [hashmap[compare],i]
            hashmap[num] = i    
        