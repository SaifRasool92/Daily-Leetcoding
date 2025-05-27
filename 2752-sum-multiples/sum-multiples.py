class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            nums.append(i)

        total_sum = 0

        for num in nums:
            if num % 3 == 0:
                total_sum += num
            elif num % 5 == 0:
                total_sum += num
            elif num % 7 == 0:
                total_sum += num

        return total_sum
            
