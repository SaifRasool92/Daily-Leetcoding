class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # largest sum
        ans = nums[0]
        win_sum = 0

        # for loop: right pointer
        for i in range(len(nums)):
            win_sum = win_sum + nums[i]
            if win_sum > ans:
                ans = win_sum
            if win_sum < 0:
                # start new window
                win_sum = 0  # reset

        return ans