class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 1):
            if (i > 0) and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                ts = nums[i] + nums[l] + nums[r]
                if ts > 0:
                    r = r - 1
                elif ts < 0:
                    l = l + 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l = l + 1
        
        return res

