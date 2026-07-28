class Solution:
    def checkIthBit(self, n: int, i: int) -> bool:
        # Your code goes here
        if n & 1<<i ==0:
            return False
        else:
            return True