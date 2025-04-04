class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen_sum = set()
        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]

            if current_sum in seen_sum:
                return True

            seen_sum.add(current_sum)

        return False