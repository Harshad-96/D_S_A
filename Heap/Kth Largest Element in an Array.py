import heapq
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # n = len(nums)
        # ans = []
        # for i in range(k):
        #     heapq.heappush(ans,nums[i])
        # for i in range(k,n):
        #     if nums[i] > ans[0]:
        #         heapq.heappop(ans)
        #         heapq.heappush(ans,nums[i])
        # return ans[0]
        n = len(nums)
        left = 0
        right = n - 1
        while True:
            pivotIndex = self.randomIndex(left,right)
            pivotIndex = self.partition(nums,pivotIndex,left,right)
            if pivotIndex == k-1:
                return nums[pivotIndex]
            elif pivotIndex > k-1:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1

    def randomIndex(self,left,right):
        return random.randint(left,right)
    
    def partition(self,nums,pivotIndex,left,right):
        pivot = nums[pivotIndex]
        nums[left],nums[pivotIndex] = nums[pivotIndex],nums[left]
        ind = left+1
        for i in range(ind,right+1):
            if nums[i] > pivot:
                nums[i],nums[ind] = nums[ind],nums[i]
                ind += 1
        nums[left],nums[ind-1] = nums[ind-1],nums[left]
        return ind-1