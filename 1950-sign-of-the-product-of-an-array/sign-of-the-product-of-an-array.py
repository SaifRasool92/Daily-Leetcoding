class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for v in nums:
            if v == 0:
                return 0
            if v < 0:
                ans *= -1
        return ans

        # prod = 1
        # for num in nums:
        #     prod = prod * num
        # if prod > 0:
        #     return 1
        # elif prod < 0:
        #     return -1
        # elif prod == 0:
        #     return 0