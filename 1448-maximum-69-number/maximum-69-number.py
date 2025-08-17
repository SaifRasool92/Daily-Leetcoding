class Solution:
    def maximum69Number (self, num: int) -> int:
        # ans = list(str(num))
        # for i in range(len(ans)):
        #     if ans[i] == '6':
        #         ans[i] = '9'
        #         break
        # return int("".join(ans))

        return int(str(num).replace('6', '9', 1))


class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i, digit in enumerate(num):
            if digit == "6":
                return int(num[:i] + "9" + num[i+1:])
        return int(num)