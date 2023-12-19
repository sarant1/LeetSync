class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0 or matrix[i][j] == "0":
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = min(min(matrix[i-1][j-1], matrix[i-1][j]), matrix[i][j-1])+1
                if matrix[i][j] > ans:
                    ans = matrix[i][j]
        print(matrix)
        return ans*ans


        
        

        