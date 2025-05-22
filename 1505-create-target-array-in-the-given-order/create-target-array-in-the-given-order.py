class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(nums)):
            target.insert(index[i], nums[i])

        return target
            

# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]