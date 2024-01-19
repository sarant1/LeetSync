class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}
        def dfs(row, i):
            if (row, i) in cache:
                return cache[(row, i)]
            if row < 0 or row == len(matrix):
                return 0
            if i < 0 or i >= len(matrix[0]):
                return float('inf')
            total = matrix[row][i] + min(dfs(row+1,i-1), dfs(row+1,i), dfs(row+1,i+1))
            cache[(row, i)] = total
            return total
        ans = float('inf')
        for i in range(len(matrix[0])):
            ans = min(ans, dfs(0, i))
        return ans
            
        