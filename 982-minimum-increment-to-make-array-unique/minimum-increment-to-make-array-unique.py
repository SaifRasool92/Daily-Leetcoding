class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        moves = 0
        prev = float('-inf')
        for num in nums:
            if num <= prev:
                prev += 1
                moves += prev - num
            else:
                prev = num
        return moves

        # 2nd Method
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        seen = set()
        moves = 0
        for num in nums:
            while num in seen:
                num += 1
                moves += 1
            seen.add(num)
        return moves

        # 3rd Method

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                inc = nums[i - 1] - nums[i] + 1
                nums[i] += inc
                moves += inc
        return moves

        # 4th Method

# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:

#         pos = {}
#         moves = 0

#         for num in nums:
#             if num not in pos:
#                 pos[num] = num
#             else:
#                 curr = pos[num] + 1
#                 while curr in pos:
#                     curr += 1
#                 pos[curr] = curr
#                 pos[num] = curr
#                 moves += curr - num
#         return moves


