class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #  matrix = [[1,2,3], -> [3,2,1]
        #            [4,5,6], -> [6,5,4]
        #            [7,8,9]] -> [9,8,7]
        
        for i in range(len(matrix)):  # -> 3
            for j in range(i+1, len(matrix[0])): # -> 1,2
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                # matrix[0][1], matrix[1][0] = matrix[1][0], matrix[0][1]
                # matrix[0][2], matrix[2][0] = matrix[2][0], matrix[0][2]
                
                # matrix[1][2], matrix[2][1] = matrix[2][1], matrix[1][2]
        
        for i in range(len(matrix)): #4
            matrix[i].reverse()
        
                
               #  matrix = [[1,2,3], | [[1,4,7],
        #                   [4,5,6], |  [2,5,8],
        #                   [7,8,9]] |  [3,6,9]]