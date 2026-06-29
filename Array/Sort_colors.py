class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = 0
        for num in nums:
            if num == 0:
                i += 1
            elif num == 1:
                j += 1
            else:
                k += 2
        nums[:i] = [0] * i
        nums[i:j] = [1] * j
        nums[j:k] = [2] * k
        print(i,j,k)
                       
    nums = [2,0,2,1,1,0]    
    sortColors(self,nums)