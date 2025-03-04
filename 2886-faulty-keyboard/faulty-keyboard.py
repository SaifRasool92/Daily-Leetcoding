class Solution:
    def finalString(self, s: str) -> str:
        result = [] 
        for char in s:  #s = "string"
            if char == 'i':
                result.reverse()
            else:
                result.append(char)
        
        return ''.join(result)