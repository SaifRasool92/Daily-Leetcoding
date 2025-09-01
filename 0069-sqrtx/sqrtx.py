class Solution:
    def mySqrt(self, x: int) -> int:
        # if x==0:
        #     return 0
        # for i in range(1,x+1):
        #     if i*i == x:
        #         return i
        #     elif i*i > x:
        #         return i-1

        left = 1
        right = x

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return right