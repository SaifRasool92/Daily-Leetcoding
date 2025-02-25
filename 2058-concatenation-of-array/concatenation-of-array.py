class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums) * 2
        ans = []
        for i in range(length):
            ans.append (nums [i % len(nums)] )
        return ans