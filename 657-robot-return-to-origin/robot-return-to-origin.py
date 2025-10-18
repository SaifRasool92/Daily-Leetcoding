class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        freq = {'R':2, 'D':2}
        """
        freq = Counter(moves)
        if freq['L'] == freq['R'] and freq['U'] == freq['D']:
            return True
        return False