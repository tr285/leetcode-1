class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = set()
        cols = set()
        m = len(matrix)
        n= len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0:
                   row.add(i)
                   cols.add(j)
        for i in row:
            for j in range(n):
                matrix[i][j] =0
        for j in cols:
            for i in range(m):
                matrix[i][j] =0