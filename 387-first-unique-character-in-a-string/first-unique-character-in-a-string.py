class Solution:
    def firstUniqChar(self, s: str) -> int:
        myDict = { }

        for char in s:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict[char] = 1
        
        for i, char in enumerate(s):
            if myDict[char] == 1:
                return i
        return -1