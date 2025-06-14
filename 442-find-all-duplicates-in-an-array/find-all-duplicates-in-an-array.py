class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1           # map value → index (0‑based)
            if nums[idx] < 0:            # we’ve visited before → duplicate
                res.append(abs(num))
            else:                        # first visit → mark as seen
                nums[idx] = -nums[idx]
        return res

        
        # s = set()
        # sol = []

        # for i in nums:
        #     if i in s:
        #         sol.append(i)
        #     else:
        #         s.add(i)
        # return sol