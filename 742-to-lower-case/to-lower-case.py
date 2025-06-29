class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()

        result = ''
        for char in s:
            if char.isupper():
                char = char.lower()
                result += char
            else:
                result += char
        return result
