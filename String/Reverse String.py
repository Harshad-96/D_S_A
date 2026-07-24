# class Solution(object):
#     def rotateString(self, s, goal):
#         """
#         :type s: str
#         :type goal: str
#         :rtype: bool
#         """
#         n = len(s)
#         m = len(goal)
#         if n != m:
#             return False
#         i = 0
#         j = 0
#         while j < m:
#             rev = goal[:j][::-1]
#             rev2 = goal[j:][::-1]
#             rev3 = rev + rev2
#             ans = rev3[::-1]
#             if s == ans:
#                 return True
#             else:
#                 j += 1
#         return False
# optimal solution

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)
        m = len(goal)
        if n != m:
            return False
        i = 0
        j = 0
        strr = s + s
        if goal in strr:
            return True
        else:
            return False