class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        return self.helper(clean,0)
    def helper(self,s,left):
        n = len(s)
        if left >= n//2:
            return True
        if s[left] != s[n-1-left]:
            return False
        return self.helper(s,left+1)