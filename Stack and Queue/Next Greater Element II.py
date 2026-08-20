class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []          
        ans = [-1] * n

        for i in range(2 * n - 1, -1, -1):     
            idx = i % n
            while stack and nums[stack[-1]] <= nums[idx]:
                stack.pop()
            if i < n:                             
                ans[idx] = nums[stack[-1]] if stack else -1
            stack.append(idx)

        return ans