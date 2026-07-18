class Solution:
    def ispossible(self,nums,mid,m):
        n = len(nums)
        student = 1
        pages = 0
        for i in range(n):
            if pages+nums[i] > mid:
                student += 1
                pages = nums[i]
            else:
                pages +=  nums[i]
        if student > m:
            return False
        else:
            return True



    def findPages(self, nums, m):
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high)//2
            if self.ispossible(nums,mid,m):
                high = mid - 1
            else:
                low = mid + 1
        return low
        
       