class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1] = 1

        def dfs(x, y):
            if x >= len(obstacleGrid) or y >= len(obstacleGrid[0]) or obstacleGrid[x][y]:
                return 0
            if dp[x][y]:
                return dp[x][y]
            dp[x][y] = dfs(x+1,y) + dfs(x,y+1)
            return dp[x][y]
        return dfs(0,0)
         
