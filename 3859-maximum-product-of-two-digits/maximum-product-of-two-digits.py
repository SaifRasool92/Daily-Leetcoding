class Solution:
    def maxProduct(self, n: int) -> int:

        s = str(n)
        sorted_digits = sorted(s)
        return (int(sorted_digits[-1]) * int(sorted_digits[-2]))