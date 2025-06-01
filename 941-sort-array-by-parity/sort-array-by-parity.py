class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.insert(0, num)
            elif num % 2 != 0:
                ans.append(num)

        return ans