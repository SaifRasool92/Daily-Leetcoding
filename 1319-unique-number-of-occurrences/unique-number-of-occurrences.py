class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        int_count = {}

        for digit in arr:
            if  digit in int_count:
                int_count[digit] +=1
            else:
                int_count[digit] = 1

        occurances = list(int_count.values())
        for i in range(len(occurances)):
            for j in range(i+1,len(occurances)):
                if occurances[i] == occurances[j]:
                    return False
        return True