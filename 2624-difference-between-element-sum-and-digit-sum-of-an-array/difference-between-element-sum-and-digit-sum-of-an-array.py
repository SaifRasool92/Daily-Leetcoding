class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            while num > 0:
                digit_sum += num % 10
                num //= 10
        answer = abs(element_sum - digit_sum)
        return answer

        # element_sum = sum(nums)
        # digit_sum_str = ""
        # for i in nums:
        #     digit_sum_str.append(str(i))
        # digit_sum_str = list(digit_sum_str)
        # digit_sum = sum(digit_sum_str)

        # abs_diff = abs(element_sum - digit_sum)

        # return abs_diff