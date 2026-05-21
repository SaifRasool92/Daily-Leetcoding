class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = ""
        for char in s:
            if char.isupper():
                new_s += chr(ord(char)-ord("A")+ord("a"))
            else:
                new_s += char
                
        return new_s


    # 2nd approach
    #return s.lower()