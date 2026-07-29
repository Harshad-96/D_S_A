class Solution:
    def secondLargestElement(self, nums):
        large = nums[0]
        secont_large = -1
        for num in nums:
            if num > large:
                secont_large = large
                large = num
            elif num < large and num > secont_large:
                secont_large = num
        return secont_large
        