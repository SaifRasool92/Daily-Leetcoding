class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            # Step 1: Find the candidate for majority element
            
            candidate = None
            count = 0
            for num in nums:
                if count == 0:
                    candidate = num
                # if num == candidate:
                #     count += 1
                # else:
                #     count -= 1
                count += (1 if num == candidate else -1) #you can also write this single line
            
            # Step 2: Return the candidate
            return candidate

    # Method 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 # 1
        cand = None # 3
        for num in nums: # nums = [3,2,3]
            if count == 0:
                cand = num
            if num == cand:
                count +=1
            else:
                count -= 1
        return cand