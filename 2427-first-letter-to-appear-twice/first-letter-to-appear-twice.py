class Solution:
    def repeatedCharacter(self, s: str) -> str:

        empty_set = []
        for i in s: 
            if i in empty_set:
                return i

            empty_set.append(i)