class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_1 = []
        nums_2 = []
        for num in set(nums1):
            if num not in nums2:
                nums_1.append(num)
        for num in set(nums2):
            if num not in nums1:
                nums_2.append(num)

        return nums_1, nums_2

# 2nd Method       
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        nums_1 = list(set1 - set2)
        nums_2 = list(set2 - set1)
        
        return [nums_1, nums_2]

         