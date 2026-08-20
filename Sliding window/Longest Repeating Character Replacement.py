class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        maxlen = 0
        maxfreq = 0
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1
            maxfreq = max(maxfreq,dic[s[i]])
            if (i - l + 1) - maxfreq > k:
                dic[s[l]] -= 1
                l += 1
            maxlen =  max(maxlen,i-l+1)
        return maxlen