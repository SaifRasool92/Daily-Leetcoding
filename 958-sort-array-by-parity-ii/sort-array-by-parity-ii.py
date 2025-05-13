class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = []
        even = []
        odd = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            elif num % 2 != 0:
                odd.append(num)
                
        for i in range(len(even)):  
            ans.append(even[i])
            ans.append(odd[i])
            
        return ans
            

