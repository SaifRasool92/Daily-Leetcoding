class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums) # 28
        left_sum = 0

        for i in range(len(nums)):

            right_sum = total_sum - left_sum - nums[i] # 28 - 0 - 1

            if left_sum == right_sum :
                return i

            left_sum += nums[i]

        return -1