class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums1 = set(nums1)  
        nums2 = set(nums2)  

        for num in nums2:
            if num in nums1:
                answer.append(num)
                

        return answer

# Method 2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result =[]        
        for num in nums1:  
            if num in nums2 and num not in result:
                result.append(num)
        return result


# 3 Method
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))


# 4 Method

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        intersection = set()
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                intersection.add(nums1[i])
                i += 1
                j += 1
        
        return list(intersection)
