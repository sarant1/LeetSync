class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i > 0 and i < n and j>0 and j < m-1:
                    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1]) 
                elif i > 0 and i < n and j==0:
                    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j],matrix[i-1][j+1]) 
                elif i > 0 and i < n and j==m-1:
                    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j], matrix[i-1][j-1]) 
        return min(matrix[n-1])

            
        