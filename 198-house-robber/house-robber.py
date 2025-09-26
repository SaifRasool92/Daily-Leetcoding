class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = 0
        r2 = 0
        for n in nums:
            temp = max(r1 + n, r2)
            r1 = r2
            r2 = temp
        return r2    

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)               # memoize subproblems
        def helper(i: int) -> int:
            if i >= len(nums):         # base case: past the last house
                return 0
            # Choose: rob this house + skip next, OR skip this house
            return max(nums[i] + helper(i + 2),
                       helper(i + 1))
        return helper(0)