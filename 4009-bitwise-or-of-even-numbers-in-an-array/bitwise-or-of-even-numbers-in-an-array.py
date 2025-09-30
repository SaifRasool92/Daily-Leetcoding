class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if not nums[i] & 1:
                res |= nums[i]
        return res

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if num % 2 == 0:   # check if even
                result |= num  # OR operation
        return result
