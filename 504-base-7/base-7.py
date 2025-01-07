class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
         return "0"
        result =""
        is_negative = num < 0
        num = abs(num)
        while num > 0:
            result= str(num % 7)+ result
            num //= 7
        if(is_negative):
            result = "-"+result
        return result



# # Example usage:
# solution = Solution()
# print(solution.convertToBase7(100))  # Output: "202"
# print(solution.convertToBase7(-7))   # Output: "-10"
