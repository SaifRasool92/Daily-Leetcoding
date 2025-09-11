# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
            
#         nums = sorted(set(nums))
#         result = []
        
#         for i in range(len(nums)):  #nums = [1,2,3,4,100,200]
#             if i > 0 :
#                 if nums[i] == nums[i-1]+1   :
#                     result.append(i)
                
#         return len(result)
        


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = sorted(set(nums))
        result = []
        current = 1   # at least one number exists

        for i in range(1, len(nums)):  # start from index 1
            if nums[i] == nums[i-1] + 1:    #nums = [1,2,3,4,100,200,201,202,203,204,205]
                current += 1
            else:
                result.append(current)
                current = 1

        result.append(current)  # push last streak
        return max(result)

                
                
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         nums = sorted(set(nums))  # remove duplicates + sort
#         longest = 1
#         current = 1

#         for i in range(1, len(nums)): #nums = [1,2,3,4,100,200]
#             if nums[i] == nums[i-1] + 1:
#                 current += 1
#                 longest = max(longest, current)
#             else:
#                 current = 1  # reset streak

#         return longest

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for num in numSet:
#             if (num - 1) not in numSet:
#                 length = 1
#                 while (num + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest
        