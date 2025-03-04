from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        while nums:
            if len(nums) == 1:
                total += nums.pop()
            else:
                first = nums.pop(0)  # Remove first element
                last = nums.pop(-1)  # Remove last element
                total += int(str(first) + str(last))  # Concatenate and add
        return total
