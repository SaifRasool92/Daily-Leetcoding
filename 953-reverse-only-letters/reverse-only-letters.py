class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in alphas:
                i += 1
            elif s[j] not in alphas:
                j -= 1  # Fixed: Move j left instead of right
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1  # Fixed: Move j left after swapping
        
        return "".join(s)



        #......Second Method......
        # s = list(s)  # Convert string to list for modification
        # i, j = 0, len(s) - 1

        # while i < j:
        #     if not s[i].isalpha():
        #         i += 1
        #     elif not s[j].isalpha():
        #         j -= 1
        #     else:
        #         s[i], s[j] = s[j], s[i]
        #         i += 1
        #         j -= 1
        
        # return "".join(s)

