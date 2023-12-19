class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0" or i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])+1
                ans = max(ans, matrix[i][j])
        return ans*ans


        
        

        