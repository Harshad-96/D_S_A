class Solution:
    def prefixToInfix(self, s: str) -> str:
        # Your code goes here
        p = {'+','-','*','/','^'}
        stack = []
        
        n = len(s)
        i = n-1
        while i >= 0:
            if s[i] == " ":
                pass
            elif s[i] in p:
                op1 = stack.pop()
                op2 = stack.pop()
                combine = "(" + op1 + s[i] + op2 + ")"
                stack.append(combine)
            else:
                stack.append(s[i])
            i -= 1
        return stack[-1]
    