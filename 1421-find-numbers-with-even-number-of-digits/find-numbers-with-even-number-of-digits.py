class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # count = 0
        # for num in nums:
        #     if len(str(num)) % 2 == 0:
        #         count +=1
        # return count
        return sum(1 for num in nums if len(str(num)) % 2 == 0)