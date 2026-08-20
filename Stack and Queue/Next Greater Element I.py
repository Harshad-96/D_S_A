class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        greater = {}
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            greater[num] = stack[-1] if stack else -1
            stack.append(num)
        ans = []
        for num in nums1:
            ans.append(greater[num])
        return ans
        