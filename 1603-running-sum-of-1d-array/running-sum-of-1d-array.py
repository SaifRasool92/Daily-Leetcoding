class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        for i in range(len(nums)):
            temp = temp + nums[i]
            nums[i] = temp
        return nums


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        for i in range(len(nums)):
            nums[i] = nums[i] + prev
            prev = nums[i]
        return nums

#Brute Force:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(sum(nums[:i+1]))
        return result
# Optimezed Solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum
        return nums

# More Optimized
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums