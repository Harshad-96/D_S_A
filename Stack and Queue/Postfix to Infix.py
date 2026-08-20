class Solution:
    def post_to_infix(self, post_exp: str) -> str:
        # Your code goes here
        p = {'+','-','*','/','^'}
        stack = []
        for ch in post_exp:
            if ch == " ":
                continue
            elif ch in p:
                op2 = stack.pop()
                op1 = stack.pop()
                combine = "(" + op1 + ch + op2 + ")" 
                stack.append(combine)
            else:
                stack.append(ch)
        return stack[-1]
    