class Solution:
    def repeatedCharacter(self, s: str) -> str:
        array = []
        for i in s:
            if i in array:
                return i

            array.append(i)
            
        #....2nd Method...(using set)
        # empty_set = []
        # for i in s: 
        #     if i in empty_set:
        #         return i

        #     empty_set.append(i)