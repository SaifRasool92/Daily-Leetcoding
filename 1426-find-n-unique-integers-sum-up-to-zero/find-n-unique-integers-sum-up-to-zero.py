class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []

        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)

        if n % 2 == 1:
            result.append(0)

        return result
        
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 != 0:
            n -= 1
            res.append(0)
        cur = 1
        for i in range(0,n,2):
            res.append(cur)
            res.append(-cur)
            cur += 1
        return res
