class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        def find_missing(grid):
            n = len(grid) ** 2
            elements = []
            for nums in grid:
                for num in nums:
                    elements.append(num)

            unique = set(elements)
            total_sum = n * (n + 1) // 2
            grid_sum = sum(unique)
            missing = total_sum - grid_sum
            return missing

        def find_repeat(elements):
            """This will find repeat element"""
            repeat = 0
            for num in elements:
                if elements.count(num) > 1:
                    repeat = num
                    break
            return repeat

        # Create elements list once
        elements = []
        for nums in grid:
            for num in nums:
                elements.append(num)

        repeat = find_repeat(elements)
        missing = find_missing(grid)

        return [repeat, missing]

                
# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        
        
# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:                     