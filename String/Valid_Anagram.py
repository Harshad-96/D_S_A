class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        mapp = {}
        if n != m:
            return False
        for ch in s:
            mapp[ch] = mapp.get(ch,0) + 1
        for ch in t:
            if ch not in mapp: 
                    return False
            else:
                if mapp[ch] == 0:
                    return False
                else:
                    mapp[ch] -= 1
        return True