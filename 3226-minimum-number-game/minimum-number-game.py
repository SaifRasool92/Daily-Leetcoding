class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(0, len(nums), 2):
            alice = nums[i]
            bob = nums[i + 1]
            arr.append(bob)   # Bob appends first
            arr.append(alice) # Then Alice appends
        return arr

        # n = len(nums)
        # nums.sort()
        # for i in range(0, n, 2):
        #     if i + 1 < n:
        #         nums[i], nums[i + 1] = nums[i + 1], nums[i]
        # return nums