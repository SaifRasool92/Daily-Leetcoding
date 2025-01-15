class Solution:
    def firstUniqChar(self, s: str) -> int:
            # Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Find the first character with a count of 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # No unique character found
        return -1