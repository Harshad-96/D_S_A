class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pos = 0
        nig = 1
        ans = [0] * n
        for i in range(0,n):
            if nums[i] > 0 :
                ans[pos] += nums[i]
                pos += 2
            else:
                ans[nig] += nums[i]
                nig += 2
        return ans
        

        