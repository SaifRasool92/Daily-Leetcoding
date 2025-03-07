class Solution:
    def repeatedCharacter(self, s: str) -> str:

        empty_set = set()  # {'a','b','c','d}
        for i in s:             # s = "abcdd"
            if i in empty_set:
                return i

            empty_set.add(i)