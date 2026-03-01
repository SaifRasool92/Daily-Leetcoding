class Solution:
    def majorityElement(self, nums: List[int]) -> int:   
        # Phase 1
        majority = nums[0] 
        count = 1    
        for i in range(1,len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = nums[i]
                    count = 1  
                    
        # Phase 2
        count = 0   
        for i in range(len(nums)):
            if nums[i] == majority:
                count +=1
                
                
        if count > len(nums) // 2:
            return majority

        










# """ Better Approch """
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
        
        
#         ans = 0
#         n = len(nums)
#         maj =  n // 2
#         freq = {}
        
#         # nums = [2,2,1,1,1,2,2]
#         for num in nums:
#             # if num in freq:
#             #     freq[num] += 1
#             # else:
#             #     freq[num] = 1
#             freq[num] = freq.get(num, 0) + 1  # Update frequency
             
#             if freq[num] > maj:
#                 ans = num
                
#         return ans
        
        
        
        
        
        
        
     

        
        
# """Naive Approch"""                         
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#     majority = -1
#     n = len(nums)
    
#     for i in range(n):
#         count = 1
        
#         for j in range(i+1, n):
#             if nums[j] == nums[i]:
#                 count += 1
#         if count > n // 2:
#             majority = nums[i]
#     return majority