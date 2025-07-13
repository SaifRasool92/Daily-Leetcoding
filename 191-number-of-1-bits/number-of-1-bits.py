class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n:
            n &= n - 1   # remove the rightmost 1
            count += 1
        return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        for i in range(32):
            if (n >> i) & 1:  # (Right shift) AND 1
                ans += 1

        return ans

