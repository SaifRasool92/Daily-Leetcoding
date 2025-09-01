class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:   # Input: s = "([])"
            if char == '(':
                stack.append(')')

            elif char == '[':
                stack.append(']')

            elif char == '{':
                stack.append('}')

            else:

                if len(stack) == 0:
                    return False  # no matching opening bracket
                top = stack.pop()
                if char != top:
                    return False  # mismatched bracket

        return len(stack) == 0  # true if all matched     