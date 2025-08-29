class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Create a new string by repeating s twice
        doubled = s + s

        # Remove the first and last characters
        trimmed = doubled[1:-1]

        # If the original string 's' exists in the trimmed version,
        # it means 's' is made by repeating a substring
        return s in trimmed