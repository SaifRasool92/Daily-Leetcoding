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
        nums.remove(max(nums))
        nums.remove(min(nums))

        # copy_nums = nums[:] 
        # copy_nums.remove(max(copy_nums))  
        # copy_nums.remove(min(copy_nums))  

        if nums:
            return nums.pop() 
        return -1

     