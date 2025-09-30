class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if not nums[i] & 1:
                res |= nums[i]
        return res