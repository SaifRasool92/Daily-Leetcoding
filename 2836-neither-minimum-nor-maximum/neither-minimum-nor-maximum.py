class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # max_value = max(nums)
        # min_value = min(nums)
        # for i in range(len(nums)):
        #     if nums[i] not in (max_value, min_value):
        #         return nums[i]
        # return -1



        if len(nums) < 3:
            return -1  

        copy_nums = nums[:] 
        copy_nums.remove(max(copy_nums))  
        copy_nums.remove(min(copy_nums))  

        if copy_nums:
            return copy_nums.pop() 
        return -1

     