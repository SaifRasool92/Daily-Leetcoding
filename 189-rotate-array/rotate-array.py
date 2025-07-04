class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void. Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2 or k == 0:
            return
        
        k = k % n
        a = n - k
        self.reverse(nums, 0, a - 1)
        self.reverse(nums, a, n - 1)
        self.reverse(nums, 0, n - 1)
    
    def reverse(self, nums, start, end):
        i = start
        j = end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
