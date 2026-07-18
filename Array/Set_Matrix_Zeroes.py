class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        row_mat = [0]*r
        col_mat = [0]*c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_mat[i] = 1
                    col_mat[j] = 1

        for i in range(r):
            for j in range(c):
                if (row_mat[i] == 1 or col_mat[j] == 1):
                    matrix[i][j] = 0
        
        return matrix