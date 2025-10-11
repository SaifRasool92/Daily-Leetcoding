class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        Input: s1 = "this apple is sweet", s2 = "this apple is sour"
        words = this apple is sweet this apple is sour
        
        count = {'this':2, 'apple':2, 'is':2, 'sweet':1, 'sour':1}
        """
        
        words = (s1 + " "+ s2).split()
        count = {}
        
        for w in words:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
       
        ans = []
        for key in count:
            if count[key] == 1:
                ans.append(key)
        
        return ans
        