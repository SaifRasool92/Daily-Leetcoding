class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:  #nums = [4,1,2,1,2]

            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for i in dic:
            if dic[i] == 1:
                return i