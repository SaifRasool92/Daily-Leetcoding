class Solution:
    def removeOuterParentheses(self, parens: str) -> str:
        s, x = [], []
        for c in parens:
            if c == ')': 
                s.pop()
            if len(s):   
                x.append(c)
            if c == '(': 
                s.append(c)
        return ''.join(x)


# ans = removeOuterParentheses('(()())(())')
# print(ans)
# ans = removeOuterParentheses('(()())(())(()(()))')
# print(ans)
# ans = removeOuterParentheses('()()')
# print(ans)
# ans = removeOuterParentheses('(())((()()))')
# print(ans)