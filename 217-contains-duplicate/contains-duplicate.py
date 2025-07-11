class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1 = set(nums)

        return len(nums) != len(nums1)

# nums = [1,2,3,1]