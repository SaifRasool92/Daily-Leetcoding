class Solution:
    def minChanges(self, s: str) -> int:
        result = 0 # 1
        for i in range(0, len(s), 2):  # s = "1001" -> 0,4,2
            if s[i] != s[i+1]: #s[2] != s[3]
                result += 1
        return result
