class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums1 = set(nums1)  
        nums2 = set(nums2)  

        for num in nums2:
            if num in nums1:
                answer.append(num)
                

        return answer