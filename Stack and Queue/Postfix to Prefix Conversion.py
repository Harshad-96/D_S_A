class Solution:
    def postToPre(self, postfix: str) -> str:
        # Your code goes here
        p = {'+','-','*','/','^'}
        stack = []
        n = len(postfix)
        i = 0
        while i < n:
            if postfix[i] == " ":
                pass
            elif postfix[i] in p:
                op1 = stack.pop()
                op2 = stack.pop()
                combine =  postfix[i] + op2 +  op1 
                stack.append(combine)
            else:
                stack.append(postfix[i])
            i += 1
        return stack[-1]
    