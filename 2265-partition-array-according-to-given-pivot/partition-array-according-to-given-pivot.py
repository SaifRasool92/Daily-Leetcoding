class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # result = []

        # for i in range (len(nums)):
        #     if nums[i] < pivot:
        #         result.append(nums[i])

        # for j in range (len(nums)):
        #     if nums[j] == pivot:
        #         result.append(nums[j])

        # for k in range (len(nums)):
        #     if nums[k] > pivot:
        #         result.append(nums[k])

        # return result

        result = []
        for num in nums:
            if num < pivot:
                result.append(num)
        for num in nums:
            if num == pivot:
                result.append(num)
        for num in nums:
            if num > pivot:
                result.append(num)

        return result