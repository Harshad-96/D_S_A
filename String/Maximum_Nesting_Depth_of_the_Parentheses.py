class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxx = 0
        for ch in s:
            if ch == "(":
                count += 1
                maxx = max(count,maxx)
            elif ch == ")":
                count -= 1
            else:
                continue
        return maxx
        