class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lt = 0
        rt = len(arr) - 1 # arr = [0,2,1,0]

        while lt < rt:
            mid = (lt + rt) // 2 #round off to lower number

            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                rt = mid
            else:
                lt = mid

        return mid