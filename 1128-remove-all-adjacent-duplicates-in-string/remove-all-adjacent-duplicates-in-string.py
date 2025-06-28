# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         result = ""
#         for ch in s:
#             if result and result[-1] == ch:
#                 result = result[:-1]
#             else:
#                 result += ch
#         return result

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # Remove the adjacent duplicate
            else:
                stack.append(char)  # Add the character to stack
        
        return ''.join(stack)  # Convert stack to string