class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        l = 0
        r = 0
        while l < len(s) and r < len(g):
            if g[r] <= s[l]:
                r += 1
            l += 1
        return r