class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2 :
            return False
            
                
        count = 0
        for i in range(len(s)):
                    
            if s[i] == "L" :
                count += 1
                if count == 3:
                    return False
            else:
    
                count = 0
        return True

class Solution:
    def checkRecord(self, s: str) -> bool:
        # Count total number of 'A's
        if s.count('A') >= 2:
            return False
        
        # Check if there is any occurrence of "LLL"
        if "LLL" in s:
            return False
        
        return True