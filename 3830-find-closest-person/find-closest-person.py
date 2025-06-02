class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z - x) < abs(z - y):
            return 1  # Person 1 is closer
        elif abs(z - y) < abs(z - x):
            return 2  # Person 2 is closer
        else:
            return 0  # Both are equally close


        # value1 = abs(x - z)  
        # value2 = abs(y - z)  
        # if value1 < value2: 
        #     return 1
        # elif value2 < value1:
        #     return 2
        # else:
        #     return 0