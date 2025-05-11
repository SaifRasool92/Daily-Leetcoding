class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        while len(nums) != len(set(nums)): 

            nums = nums[3:]
            operations += 1
        
        return operations

        # operation = 3
        # len of nums = 9
        # len of set nums = 6
        # nums = [1,2,3,4,2,3,3,5,7]

        #  1st iteration  
        # nums = [4, 2, 3, 3, 5, 7]

        # 2nd iteration 
        # nums = [3, 5, 7]
        
        # 3rd iteration 
        # nums = []
