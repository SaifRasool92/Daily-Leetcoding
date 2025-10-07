class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        dif = max(nums) - min(nums)
        return dif * k
