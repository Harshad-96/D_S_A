class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        maxx = ""
        n = len(num)
        i = n - 1
        ind = -1
        while i >= 0:
            if int(num[i]) % 2 != 0:
                ind = i
                break
            i -= 1
        if ind == -1:
            num = ""
            return num
        return num[:ind+1]
        