class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = s.strip()
        c = b.split()
        return len(c[-1])