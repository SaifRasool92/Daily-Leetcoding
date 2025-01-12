class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        n = len(s)
        # If the string length is odd, it cannot be valid.
        if n % 2 != 0:
            return False

        # Step 1: Check from left to right
        open_possible = 0  # Number of open parentheses possible
        balance = 0  # Current balance
        for i in range(n):
            if locked[i] == '1':  # Fixed character
                balance += 1 if s[i] == '(' else -1
            else:  # Flexible character
                open_possible += 1
            # If balance goes negative beyond flexibility, it's invalid
            if balance + open_possible < 0:
                return False

        # Step 2: Check from right to left
        close_possible = 0  # Number of close parentheses possible
        balance = 0  # Current balance
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':  # Fixed character
                balance += 1 if s[i] == ')' else -1
            else:  # Flexible character
                close_possible += 1
            # If balance goes negative beyond flexibility, it's invalid
            if balance + close_possible < 0:
                return False

        # If both checks passed, it's possible to make the string valid
        return True
