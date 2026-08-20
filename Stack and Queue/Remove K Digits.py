class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        stack = []
        for i in range(n):
            while stack and k > 0 and stack[-1]>num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k > 0:
            stack.pop()
            k -= 1
        
        res = "".join(stack)
        res = res.lstrip('0')
        
        if not res:
            return "0"
        return res