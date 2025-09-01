class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        for _ in range(100):  # Arbitrary large value
            if n % 3 != 0:
                break
            n = n / 3
        return n == 1

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        if n == 0 or n % 3 != 0: return False
        return self.isPowerOfThree(n / 3)