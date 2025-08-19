class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = res = 0
        for r in range(len(nums)):
            if nums[r] != 0: 
                l = r
            else:
                while nums[l] != 0: 
                    l += 1
                res += r - l + 1
        
        return res

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = res = 0
        for x in nums:
            if x == 0:
                count += 1
                res += count
            else:
                count = 0
        return res