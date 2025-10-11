class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()

        words = s1 + s2 #->u248pl
        
        dic = {}   
        for w in words:
            if w in dic:
                dic[w] += 1 
            else:
                dic[w] = 1
        
        ans = []
        for w in dic:
            if dic[w] == 1:
                ans.append(w)
        
        return ans


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter((s1 + " " + s2).split())  #-> u786il
        return [word for word, freq in count.items() if freq == 1]  #->u894ip
