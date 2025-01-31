class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        running_sum = [nums[0]]  # Initialize the first element
        
        for i in range(1, len(nums)):
            running_sum.append(running_sum[i - 1] + nums[i])  # Add previous sum to current element
        
        return running_sum
