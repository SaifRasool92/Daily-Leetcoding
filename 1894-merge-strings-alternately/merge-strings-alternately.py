class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        i,j = 0,0
        while i< len(word1) and j< len(word2):  # word1 = "ab", word2 = "pqrs"
            merged_string.append(word1[i])
            merged_string.append(word2[j])

            i+=1
            j+=1

        merged_string.append(word1[i:])
        merged_string.append(word2[j:])

        return ''.join(merged_string)