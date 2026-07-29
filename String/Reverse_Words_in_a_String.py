class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        revStr =s[::-1]
        n = len(s)
        word = ""
        i = 0
        ans = ""
        while i < n:
            while i < n and revStr[i] != " ":
                word += revStr[i]
                i += 1
            rev = word[::-1]
            if word:
                if ans == "":
                    ans = rev
                else:
                    ans = ans + " " + rev
            word = ""
            while i < n and revStr[i] == " ":
                i += 1
        return ans
    

        