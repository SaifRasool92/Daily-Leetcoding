class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        a = sorted(nums)
        return max(a[-1]*a[-2]*a[-3], a[0]*a[1]*a[-1])
        
        # nums[-1]*nums[-2]*nums[-3] gives the product of 3 maximum number (positive)

        # nums[0]*nums[1]*nums[-1] gives the product of 2 biggest negative number          not considering the negative sign and the biggest positive number.

        
        # nums.sort()

        # product1 = nums[-1] * nums[-2] * nums[-3]

        # product2 = nums[0] * nums[1] * nums[-1]

        # return max(product1, product2)
        
        # nums = [-1, -2, -3, -4, -5, -6, -7]