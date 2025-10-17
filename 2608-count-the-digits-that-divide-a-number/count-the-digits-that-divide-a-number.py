class Solution:
    def countDigits(self, num: int) -> int:
        str_num = str(num)
        count = 0
        for val in str_num:
            if num % int(val) == 0:
                count += 1
                
        return count