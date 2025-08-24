class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high + 1) // 2) - (low // 2)

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        count = (high-low) // 2

        if low % 2 == 1 or high % 2 == 1:
            count += 1
        # else:
        #     count += 0

        return count