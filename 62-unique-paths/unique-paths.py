class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        def dfs(x, y):
            if x >= m or y >= n:
                return 0
            if dp[x][y] != -1: 
                return dp[x][y]
            if x == m - 1 and y == n - 1:
                return 1
            dp[x][y] = dfs(x + 1, y) + dfs(x, y+1)
            return dp[x][y] 
        return dfs(0, 0)
