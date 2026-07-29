class Solution:
    def countSetBits(self, n: int) -> int:
        # Your code goes here
        count = 0
        while n != 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count