class Solution:
    def infix_to_prefix(self, infix: str) -> str:
        # Your code goes here
        p = {'+':1,'-':1,'*':2,'/':2,'^':3}
        def isOperator(ch):
            return ch in p
        reverse_s = ""
        for ch in reversed(infix):
            if ch == "(":
                reverse_s += ")"
            elif ch ==")":
                reverse_s += "("
            else:
                reverse_s += ch
  
        stack = []
        result = ""
        for ch in reverse_s:
            if ch == " ":
                continue
            elif ch == "(":
                stack.append(ch)
            elif ch ==")":
                while (stack and stack[-1] != "("):
                    result += stack.pop()
                stack.pop()
            elif isOperator(ch):
                while (stack and stack[-1] != "(" and p[stack[-1]] >= p[ch]):
                    result += stack.pop()
                stack.append(ch)
            else:
                result += ch
        while stack:
            result += stack.pop()
        result = result[::-1]
        return result
            