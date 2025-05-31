class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if i in ans:
                continue
            else:
                ans.append(i)
        ans.sort()
        if len(ans)>=3:
            return ans[-3]
        else:
            return max(ans)