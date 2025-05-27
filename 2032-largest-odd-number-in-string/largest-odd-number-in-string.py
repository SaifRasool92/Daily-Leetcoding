class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)- 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""  

        
        # i = len(num)
        
        # while i > 0:
        #     last_digit = int(num[i - 1])
            
        #     if last_digit % 2 != 0:
        #         result = ""
        #         for j in range(i):
        #             result += num[j]
        #         return result
            
        #     i -= 1

        # return ""