class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        ans = start ^ goal
        count = 0
        bit = 0
        while ans != 0:
            if ans & 1:
                bit += 1
            ans = ans >> 1
        return bit
        