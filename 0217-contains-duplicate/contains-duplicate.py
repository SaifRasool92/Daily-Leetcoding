class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums1 = set()
        for num in nums:
            if num in nums1:
                return True
            else:
                nums1.add(num)
        return False

        # nums1 = set(nums)
        # return len(nums) != len(nums1)

