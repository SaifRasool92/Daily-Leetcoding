class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        

        # Process first string s
        for char in s:
            if char != '#':
                stack_s.append(char)
            elif stack_s:
                stack_s.pop()

        # Process second string t
        for char in t:
            if char != '#':
                stack_t.append(char)
            elif stack_t:
                stack_t.pop()

        # Compare final processed versions of both stacks
        return stack_s == stack_t