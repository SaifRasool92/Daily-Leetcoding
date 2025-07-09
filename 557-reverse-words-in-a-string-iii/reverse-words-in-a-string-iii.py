# class Solution:
#     def reverseWords(self, s: str) -> str:
#         ans = []
#         s = s.split()
#         for char in s:  
#             l = 0
#             r = len(char) -1
#             while l < r:
#                 char[l], char[r] = char[r], char[l]
#                 l += 1
#                 r -= 1
#             ans.append(char)

#         return ' '.join(ans)

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        s = s.split()
        for char in s:
            char = list(char)      # convert string to list of chars
            l = 0
            r = len(char) - 1
            while l < r:
                char[l], char[r] = char[r], char[l]
                l += 1
                r -= 1
            ans.append(''.join(char))   # convert list back to string
        return ' '.join(ans)
