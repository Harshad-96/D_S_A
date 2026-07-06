class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        n = len(nums)
        ans = tuple(nums)
        out = 1
        for i in range(n-1):
            if (ans[i]+1) == ans[i+1]:
                out += 1
        return out

    

sol = Solution()
print(sol.longestConsecutive( [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))