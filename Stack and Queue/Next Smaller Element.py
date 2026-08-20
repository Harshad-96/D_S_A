class Solution:
    def nextSmallerElements(self, arr):
        # Your code goes here
        stack = []
        ans = []
        for num in reversed(arr):
            while stack and stack[-1] >= num:
                stack.pop()
            if stack :
                ans.append(stack[-1]) 
            else:
                ans.append(-1)
            stack.append(num)
        return reversed(ans)