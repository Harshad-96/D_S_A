class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapp = {}
        result = ""
        n = len(s)
        for ch in s:
            mapp[ch] = mapp.get(ch,0) + 1
        sorted_map = sorted(mapp.items(),key = lambda x : (-x[1],x[0]))
        for ch,freq in sorted_map:
            result = result + (ch*freq)
        return result