class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2
        elements = []
        for nums in grid:
            for num in nums:
                elements.append(num)
        unique = set(elements)
        
        total_sum = n * (n+1) // 2
        grid_sum  = sum(unique)
        
        missing = total_sum - grid_sum
        repeat = 0
        for num in elements:
            if elements.count(num) > 1:
                repeat = num
                break
        
        return [repeat, missing]

                
                