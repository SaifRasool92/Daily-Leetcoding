class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        from collections import Counter


        # Count frequencies of each character
        freq = Counter(s)
        
        # Count characters with odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)
        
        # Check the two conditions
        return k <= len(s) and k >= odd_count