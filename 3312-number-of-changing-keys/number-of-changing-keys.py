class Solution:
    def countKeyChanges(self, s: str) -> int:
        chars = s.lower()
        count = 0
        for i in range(len(chars)-1):
            if chars[i] != chars[i+1]:
                count += 1

        return count
