class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        value1 = abs(x - z)  # 2 - 4 = 2
        value2 = abs(y - z)  # 7 - 4 = 3
        if value1 < value2:  # x = 2, y = 7, z = 4
            return 1
        elif value2 < value1:
            return 2
        else:
            return 0