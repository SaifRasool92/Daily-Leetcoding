class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for i in s:
            if i == 'i':
                result.reverse()
            else:
                result.append(i)
        
        return ''.join(result)