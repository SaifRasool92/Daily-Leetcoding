class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        empty = []
        for num in x:
            empty.append(num)

        l = 0
        r = len(empty) - 1
        while l < r:
            empty[l], empty[r] = empty[r], empty[l]
            l += 1
            r -= 1
        empty = ''.join(empty)

        return int(empty) == int(x)

        """2nd Method"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        reversed_str = ""
        for char in x_str:
    #here the sequence of 'char' and 'reverse_str' matters
            reversed_str = char + reversed_str
        return reversed_str == x_str