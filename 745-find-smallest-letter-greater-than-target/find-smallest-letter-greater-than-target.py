class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 
        There are at least two different characters in letters.

        Return the smallest character in letters that is lexicographically greater than target. If such a character does 
        not exist, return the first character in letters.

        Example 1:

        Input: letters = ["c","f","j"], target = "a"
        Output: "c"
        Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

        Example 2:
        Input: letters = ["c","f","j"], target = "c"
        Output: "f"
        Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

        Example 3:
        Input: letters = ["x","x","y","y"], target = "z"
        Output: "x"
        Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
        """
        l = 0
        r = len(letters) - 1
        result = letters[0]  # default wrap-around

        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                result = letters[mid]    # candidate
                r = mid - 1
            else:   # letters[mid] <= target
                l = mid + 1
        
        return result
