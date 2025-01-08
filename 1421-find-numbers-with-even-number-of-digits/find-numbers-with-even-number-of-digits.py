class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        return sum(1 for num in nums if len(str(num)) % 2 == 0)
        # 2nd Method
        # count = 0
        # for num in nums:
        #     if len(str(num)) % 2 == 0:
        #         count +=1
        # return count