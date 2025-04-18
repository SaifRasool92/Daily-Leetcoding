class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans =  nums + nums
        # return ans
        # Input: nums = [1,2,1]
        # Output: [1,2,1,1,2,1]

        ans = []

        for j in range(2):
            for i in nums:
                ans.append(i)

        return ans

