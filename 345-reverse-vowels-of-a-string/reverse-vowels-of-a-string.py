class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        left, right = 0, len(s)-1

        while left < right:

            if s[left] not in vowels:
                left += 1

            elif s[right] not in vowels:
                right -= 1

            else:
                s[left] , s[right] = s[right] , s[left]
                left += 1
                right -= 1

        return ''.join(s)