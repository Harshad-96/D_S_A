class Solution:
    def prefixToPostfix(self, s: str) -> str:
        # Your code goes here
        p = {'+','-','*','/','^'}
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == " ":
                pass
            elif s[i] in p:
                op1 = stack.pop()
                op2 = stack.pop()
                combine =  op1 + op2 + s[i] 
                stack.append(combine)
            else:
                stack.append(s[i])
            i += 1
        return stack[-1]
    