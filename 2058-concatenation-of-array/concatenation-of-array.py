class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans =  nums + nums
        # return ans
        # Input: nums = [1,2,1]
        # Output: [1,2,1,1,2,1] = 2n

        # ans = []

        # for j in range(2):
        #     for i in nums:
        #         ans.append(i)
        # return ans

        length = len(nums) * 2 # lenghth = 6
        ans = []
        for i in range(length): # 1 = 0, 1 ,2 ,3 
            ans.append(nums [i % len(nums)]) # len(nums) = 3 i % len(nums)

        return ans