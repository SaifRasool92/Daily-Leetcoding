# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
#         def find_missing(grid):
#             """This will find missing element"""
#             n = len(grid) ** 2
#             elements = []
#             for nums in grid:
#                 for num in nums:
#                     elements.append(num)

#             unique = set(elements)
#             total_sum = n * (n + 1) // 2
#             grid_sum = sum(unique)
#             missing = total_sum - grid_sum
#             return missing

#         def find_repeat(elements):
#             """This will find repeat element"""
#             repeat = 0
#             for num in elements:
#                 if elements.count(num) > 1:
#                     repeat = num
#                     break
#             return repeat

#         # Create elements list once
#         elements = []
#         for nums in grid:
#             for num in nums:
#                 elements.append(num)

#         repeat = find_repeat(elements)
#         missing = find_missing(grid)

#         return [repeat, missing]

                
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #[[9,1,7],
        # [8,9,2],
        # [3,4,6]]
        n = len(grid)
        N = n * n
        actualSum = 0
        actualSquareSum = 0
        
        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                actualSum += num
                actualSquareSum += num * num
                
        expectedSum = (N * (N+1)) // 2
        expectedSquareSum = (N * (N + 1)* (2*N + 1)) // 6
        
        sumDifference = actualSum - expectedSum
        squareSumDifference = actualSquareSum - expectedSquareSum
        
        sum_ab = squareSumDifference // sumDifference
        repeated = (sum_ab + sumDifference) // 2
        missing = (sum_ab - sumDifference) // 2
        
        return [repeated, missing]
        
        
        

                
                