class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # prefix_0 = remove

        return haystack.find(needle)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
