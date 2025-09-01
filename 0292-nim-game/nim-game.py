class Solution:
    def canWinNim(self, n: int) -> bool:
        # for i in range(n+1):
            if n % 4 == 0:
                return False
            else:
                return True