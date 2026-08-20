class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        l = 0
        r = 0
        dic = {}
        maxlen = 0
        while r <= n-1:
            if s[r] in dic and l <= dic[s[r]]:
                l = dic[s[r]]+1
                maxlen = max(maxlen,r-l+1)
                dic[s[r]] = r
                r += 1
            else:
                maxlen = max(maxlen,r-l+1)
                dic[s[r]] = r
                r += 1
        return maxlen