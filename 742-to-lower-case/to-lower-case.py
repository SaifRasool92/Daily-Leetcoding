class Solution:
    def toLowerCase(self, s: str) -> str:
        """Hello"""
        lowerCaseLetter = ''
        for char in s:
            if char >= 'A' and char <= 'Z':
                lowerCaseLetter += chr(ord(char)+32)
            else:
                lowerCaseLetter += char
        return lowerCaseLetter        
        