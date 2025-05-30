class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        l = 0
        r = len(s) - 1
        while l < r:
            s[l] , s[r] = s[r] , s[l]
            l += 1
            r -= 1
        
        return ' '.join(s)




        # s = s.strip()
        # s = list(s)
        # l = 0
        # r = len(s)-1
        # while l < r:
        #     if s[l] != '' and s[r] != '':
        #         s[l] , s[r] = s[r] , s[l]
        #         l += 1
        #         r -= 1
        #         if s[l] == '':
        #             l += 1
        #         if s[r] == '':
        #             r -= 1

        # return ''.join(s) 
