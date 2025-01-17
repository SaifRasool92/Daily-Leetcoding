class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        def is_valid(start):
            current = start
            for i in range(1, n):
                current = derived[i - 1] ^ current
            return (current ^ start) == derived[-1]

        return is_valid(0) or is_valid(1)
