class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        result = []
        
        while n > 0:
            digit = n % 10
            result.append(digit)
            n = n//10

        return prod(result) - sum(result)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        sum = 0
        product = 1

        while n > 0:

            digit = n%10

            sum += digit
            product *= digit

            n //= 10

        return product - sum