class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        lst = s.split()

        l = 0
        r = len(lst) - 1
        while l < r:
            lst[l], lst[r] = lst[r] , lst[l]
            l += 1
            r -= 1

        return ' '.join(lst)
