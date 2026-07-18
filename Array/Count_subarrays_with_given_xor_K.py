class Solution:
    def subarraysWithXorK(self, nums, k):
        xor = 0
        mapp = {0:1}
        count = 0
        n = len(nums)
        for i in range(n):
            xor = xor ^ nums[i]
            x = xor ^ k
            count += mapp.get(x,0)
            mapp[xor] = mapp.get(xor,0) + 1
        return count