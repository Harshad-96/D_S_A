class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapp_stot = {}
        mapp_ttos = {}
        n = len(s)
        m = len(t)
        if n != m:
            return False
        for i in range(n):
            if s[i] in mapp_stot:
                if mapp_stot[s[i]] != t[i]:
                    return False
            else:
                mapp_stot[s[i]] = t[i]

            if t[i] in mapp_ttos:
                if mapp_ttos[t[i]] != s[i]:
                    return False
            else:
                mapp_ttos[t[i]] = s[i]
        return True