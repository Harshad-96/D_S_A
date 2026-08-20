class Solution:
    def infixToPostfix(self, s: str) -> str:
        # Your code goes here
        precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

        def isOperator(ch):
            return ch in precedence
        stack = []
        result = ""
        for ch in s:
            if ch == " ":
                continue
            elif ch.isalnum():
                result += ch
            elif ch == "(":
                stack.append(ch)
            elif ch == ")":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
            elif isOperator(ch):
                while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[ch] or
                    (precedence[stack[-1]] == precedence[ch] and ch != '^'))):
                    result += stack.pop()
                stack.append(ch)
        while stack:
                result += stack.pop()
        return result