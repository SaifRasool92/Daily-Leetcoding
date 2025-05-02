class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1st Method
        ans = []
        for j in range(2):
            for i in nums:
                ans.append(i)
        return ans

        # 2nd Method
        # length = len(nums) * 2 
        # ans = []
        # for i in range(length): 
        #     ans.append(nums [i % len(nums)]) 

        # return ans

        # 3rd Method but not recommended
        # ans =  nums + nums
        # return ans