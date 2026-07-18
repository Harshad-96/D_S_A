class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        indx = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                indx = i
                break
        if indx == -1:
            nums[:] = nums[:][::-1]
            return nums
        else:

            for i in range(n-1,indx,-1):
                if nums[i] > nums[indx]:
                    nums[i],nums[indx] = nums[indx],nums[i]
                    break
            nums[indx+1:] = nums[indx+1:][::-1]
            return nums 
        