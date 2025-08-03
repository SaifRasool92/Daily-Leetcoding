class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):  # Loop from end to start
            if int(num[i]) % 2 == 1:  # Check if digit is odd
                return num[:i+1]  # Return string up to that digit
        return ""  # Return empty string if no odd digit found
