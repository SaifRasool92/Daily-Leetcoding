class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x): 
            return ''.join(sorted(str(x)))

        target = ''.join(sorted(str(n)))
        for i in range(31):
            if count_digits(1 << i) == target: 
                return True
        return False

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Convert number to a sorted string of its digits
        sorted_n = sorted(str(n))
        
        # Check all powers of 2 up to the maximum possible for n's digit length
        for i in range(31):  # 2^0 to 2^30 covers up to 10^9
            if sorted(str(1 << i)) == sorted_n:
                return True
        return False